# Copyright 2022-2023 XProbe Inc.
# derived from copyright 1999-2021 Alibaba Group Holding Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ....dataframe.indexing.getitem import DataFrameIndex
from ..common.column_pruning import GetitemPruneDataSource
from .core import register_operand_based_optimization_rule


@register_operand_based_optimization_rule([DataFrameIndex])
class ChunkGetitemPruneDataSource(GetitemPruneDataSource):
    """
    Prune data source via getitem.
    """
