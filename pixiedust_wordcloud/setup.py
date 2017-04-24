# -------------------------------------------------------------------------------
# Generated by PixieDust code generator
# 
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# Inherited from maven-artifact https://github.com/hamnis/maven-artifact
# -------------------------------------------------------------------------------

from setuptools import setup, find_packages
setup(name='pixiedust_wordcloud',
	  version='0.2.1',
	  description='Word Cloud Visualization Plugin for PixieDust',
	  url='https://github.com/ibm-cds-labs/pixiedust_incubator',
	  install_requires=['pixiedust', 'wordcloud'],
	  author='vabarbosa',
	  author_email='va@us.ibm.com',
	  license='Apache 2.0',
	  packages=find_packages(),
		include_package_data=True,
	  zip_safe=False
)