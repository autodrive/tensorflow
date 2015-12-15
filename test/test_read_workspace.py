import unittest
import sys
import os

build_path = os.path.abspath(os.path.join(os.curdir, '..', 'build'))
sys.path.append(build_path)

import read_workspace as rw


class TestReadWorkspace(unittest.TestCase):
    def test_remove_comments(self):
        test_string = '''# Uncomment and update the paths in these entries to build the Android demo.
#android_sdk_repository(
#    name = "androidsdk",
#    api_level = 23,
#    build_tools_version = "23.0.1",
#    # Replace with path to Android SDK on your system
#    path = "<PATH_TO_SDK>",
#)
#
#android_ndk_repository(
#    name="androidndk",
#    path="<PATH_TO_NDK>",
#    api_level=21)

new_http_archive(
  name = "gmock_archive",
  url = "https://googlemock.googlecode.com/files/gmock-1.7.0.zip",
  sha256 = "26fcbb5925b74ad5fc8c26b0495dfc96353f4d553492eb97e85a8a6d2f43095b",
  build_file = "google/protobuf/gmock.BUILD",
)
'''
        test_list = test_string.splitlines()

        rw.remove_comments(test_list)

        expected = ['', 'new_http_archive(',
                    '  name = "gmock_archive",',
                    '  url = "https://googlemock.googlecode.com/files/gmock-1.7.0.zip",',
                    '  sha256 = "26fcbb5925b74ad5fc8c26b0495dfc96353f4d553492eb97e85a8a6d2f43095b",',
                    '  build_file = "google/protobuf/gmock.BUILD",',
                    ')']

        self.assertSequenceEqual(expected, test_list)

    def test_remove_comments_pound(self):
        test_string = '''# Uncomment and update the paths in these entries to build the Android demo.
#android_sdk_repository(
#    name = "androidsdk",
#    api_level = 23,
#    build_tools_version = "23.0.1",
#    # Replace with path to Android SDK on your system
#    path = "<PATH_TO_SDK>",
#)
#
#android_ndk_repository(
#    name="androidndk",
#    path="<PATH_TO_NDK>",
#    api_level=21)

new_http_archive(
  name = "gmock_archive",
  url = "https://googlemock.googlecode.com/files/g#mock-1.7.0.zip",
  sha256 = "26fcbb5925b74ad5fc8c26b0495dfc96353f4d553492eb97e85a8a6d2f43095b",
  build_file = "google/protobuf/gmock.BUILD",
)
'''
        test_list = test_string.splitlines()

        rw.remove_comments(test_list)

        expected = ['', 'new_http_archive(',
                    '  name = "gmock_archive",',
                    '  url = "https://googlemock.googlecode.com/files/g#mock-1.7.0.zip",',
                    '  sha256 = "26fcbb5925b74ad5fc8c26b0495dfc96353f4d553492eb97e85a8a6d2f43095b",',
                    '  build_file = "google/protobuf/gmock.BUILD",',
                    ')']

        self.assertSequenceEqual(expected, test_list)