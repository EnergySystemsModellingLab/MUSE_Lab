from muse.regressions import register_regression, regression_functor
from xarray import DataArray

@register_regression
@regression_functor(
    {"a1": "GDPexp", "a2": "constant", "x0": "GDPscaleLess", "p": "GDPscaleGreater"}
)
def LogisticSigmoid2(
    self, gdp: DataArray, population: DataArray, *args, **kwargs
) -> DataArray:
    """(a2 + (a1 - a2) / (1 + (gdp / pop / x0))^p))*pop
    Logistic Sigmoid with Levenberg Marquardt Iteration Algorithm
    Population in Million, GDP in milion MUSD2010, output in bilion v-km
    """
    from numpy import power

    return 1e-3 * (
        self.coeffs.a2
        + (
            (self.coeffs.a1 - self.coeffs.a2)
            / (1 + ((gdp / population / self.coeffs.x0) ** self.coeffs.p))
        )
    ) * population
