# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
GlobalContrastRowScaler
"""

__all__ = ["GlobalContrastRowScaler"]


from sklearn.base import TransformerMixin

from ...base_transform import BaseTransform
from ...internal.core.preprocessing.normalization._globalcontrastrowscaler import \
    GlobalContrastRowScaler as core
from ...internal.utils.utils import trace


class GlobalContrastRowScaler(
        core,
        BaseTransform,
        TransformerMixin):
    """

    Normalizes columns as specified below.

    .. remarks::
        In linear classification algorithms instances are viewed as vectors
        in
        multi-dimensional space. Since the range of values of raw data varies
        widely, some objective functions do not work properly without
        normalization. For example, if one of the features has a broad range
        of
        values, the distances between points is governed by this particular
        feature. Therefore, the range of all features should be normalized so
        that each feature contributes approximately proportionately to the
        final
        distance. This can provide significant speedup and accuracy benefits.
        In
        all the linear algorithms in nimbusml (:py:class:`Logistic Regression
        <nimbusml.linear_model.LogisticRegressionClassifier>`,
        :py:class:`Averaged Perceptron
        <nimbusml.linear_model.AveragedPerceptronBinaryClassifier>`, etc.),
        the default is to normalize features before training.

        ``GlobalContrastRowScaler`` performs a global contrast normalization
        on
        input values: ``Y = (s * X - M) / D``, where s is a scale, M is mean
        and D
        is either L2 norm or standard deviation..

    :param columns: a dictionary of key-value pairs, where key is the output
        column name and value is the input column name.

        * Multiple key-value pairs are allowed.
        * Input column type:
         `Vector Type </nimbusml/concepts/types#vectortype-column>`_.
        * Output column type:
         `Vector Type </nimbusml/concepts/types#vectortype-column>`_.

        * The type of the input column is of type :
        * The type of the output column is of type
         `Vector Type </nimbusml/concepts/types#vectortype-column>`_.
        * If the output column names are same as the input column names, then
        simply specify ``columns`` as a list of strings.

        The << operator can be used to set this value (see
        `Column Operator </nimbusml/concepts/columns>`_)

        For example
         * GlobalContrastRowScaler(columns={'out1':'input1',
        'out2':'input2'})
         * GlobalContrastRowScaler() << {'out1':'input1', 'out2':'input2'}

        For more details see `Columns </nimbusml/concepts/columns>`_.

    :param sub_mean: Subtract mean from each value before normalizing.

    :param use_std_dev: Normalize by standard deviation rather than L2 norm.

    :param scale: Scale features by this value.

    :param params: Additional arguments sent to compute engine.

    .. seealso::
        :py:class:`MinMaxScaler
        <nimbusml.preprocessing.normalization.MinMaxScaler>`,
        :py:class:`Binner
        <nimbusml.preprocessing.normalization.Binner>`,
        :py:class:`MeanVarianceScaler
        <nimbusml.preprocessing.normalization.MeanVarianceScaler>`,
        :py:class:`LogMeanVarianceScaler
        <nimbusml.preprocessing.normalization.LogMeanVarianceScaler>`.

    .. index:: normalize, preprocessing

    Example:
       .. literalinclude:: /../nimbusml/examples/GlobalContrastRowScaler.py
              :language: python
    """

    @trace
    def __init__(
            self,
            sub_mean=True,
            use_std_dev=False,
            scale=1.0,
            columns=None,
            **params):

        if columns:
            params['columns'] = columns
        BaseTransform.__init__(self, **params)
        core.__init__(
            self,
            sub_mean=sub_mean,
            use_std_dev=use_std_dev,
            scale=scale,
            **params)
        self._columns = columns

    def get_params(self, deep=False):
        """
        Get the parameters for this operator.
        """
        return core.get_params(self)