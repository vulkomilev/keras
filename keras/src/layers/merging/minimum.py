from keras.src import ops
from keras.src.api_export import keras_export
from keras.src.layers.merging.base_merge import Merge


@keras_export("keras.layers.Minimum")
class Minimum(Merge):
    """Computes elementwise minimum on a list of inputs.

    It takes as input a list of tensors, all of the same shape,
    and returns a single tensor (also of the same shape).

    Examples:

    >>> input_shape = (2, 3, 4)
    >>> x1 = np.random.rand(*input_shape)
    >>> x2 = np.random.rand(*input_shape)
    >>> y = keras.layers.Minimum()([x1, x2])

    Usage in a Keras model:

    >>> input1 = keras.layers.Input(shape=(16,))
    >>> x1 = keras.layers.Dense(8, activation='relu')(input1)
    >>> input2 = keras.layers.Input(shape=(32,))
    >>> x2 = keras.layers.Dense(8, activation='relu')(input2)
    >>> # equivalent to `y = keras.layers.minimum([x1, x2])`
    >>> y = keras.layers.Minimum()([x1, x2])
    >>> out = keras.layers.Dense(4)(y)
    >>> model = keras.models.Model(inputs=[input1, input2], outputs=out)

    """

    def _merge_function(self, inputs):
        output = inputs[0]
        for i in range(1, len(inputs)):
            output = ops.minimum(output, inputs[i])
        return output


@keras_export("keras.layers.minimum")
def minimum(inputs, **kwargs):
    """Functional interface to the `keras.layers.Minimum` layer.

    Args:
        inputs: A list of input tensors , all of the same shape.
        **kwargs: Standard layer keyword arguments.

    Returns:
        A tensor as the elementwise product of the inputs with the same
        shape as the inputs.

    Examples:

    >>> input_shape = (2, 3, 4)
    >>> x1 = np.random.rand(*input_shape)
    >>> x2 = np.random.rand(*input_shape)
    >>> y = keras.layers.minimum([x1, x2])

    Usage in a Keras model:

    >>> input1 = keras.layers.Input(shape=(16,))
    >>> x1 = keras.layers.Dense(8, activation='relu')(input1)
    >>> input2 = keras.layers.Input(shape=(32,))
    >>> x2 = keras.layers.Dense(8, activation='relu')(input2)
    >>> y = keras.layers.minimum([x1, x2])
    >>> out = keras.layers.Dense(4)(y)
    >>> model = keras.models.Model(inputs=[input1, input2], outputs=out)

    """
    return Minimum(**kwargs)(inputs)
