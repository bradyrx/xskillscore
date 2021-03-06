import xarray as xr

from .deterministic import (
    effective_sample_size,
    mae,
    mape,
    median_absolute_error,
    mse,
    pearson_r,
    pearson_r_eff_p_value,
    pearson_r_p_value,
    r2,
    rmse,
    smape,
    spearman_r,
    spearman_r_eff_p_value,
    spearman_r_p_value,
)
from .probabilistic import (
    xr_brier_score as brier_score,
    xr_crps_ensemble as crps_ensemble,
    xr_crps_gaussian as crps_gaussian,
    xr_crps_quadrature as crps_quadrature,
    xr_threshold_brier_score as threshold_brier_score,
)


@xr.register_dataset_accessor('xs')
class XSkillScoreAccessor(object):
    def __init__(self, xarray_obj):
        self._obj = xarray_obj

    def _in_ds(self, x):
        """
        If x is not a string, presumably an array, return the array.
        Else x is a string, presumably within ds, return the ds variable.
        """
        if not isinstance(x, str):
            return x
        else:
            return self._obj[x]

    def pearson_r(self, a, b, dim, weights=None, skipna=False):
        a = self._in_ds(a)
        b = self._in_ds(b)
        return pearson_r(a, b, dim, weights=weights, skipna=skipna)

    def r2(self, a, b, dim, weights=None, skipna=False):
        a = self._in_ds(a)
        b = self._in_ds(b)
        return r2(a, b, dim, weights=weights, skipna=skipna)

    def pearson_r_p_value(self, a, b, dim, weights=None, skipna=False):
        a = self._in_ds(a)
        b = self._in_ds(b)
        return pearson_r_p_value(a, b, dim, weights=weights, skipna=skipna)

    def effective_sample_size(self, a, b, dim, skipna=False):
        a = self._in_ds(a)
        b = self._in_ds(b)
        return effective_sample_size(a, b, dim, skipna=skipna)

    def pearson_r_eff_p_value(self, a, b, dim, skipna=False):
        a = self._in_ds(a)
        b = self._in_ds(b)
        return pearson_r_eff_p_value(a, b, dim, skipna=skipna)

    def spearman_r(self, a, b, dim, weights=None, skipna=False):
        a = self._in_ds(a)
        b = self._in_ds(b)
        return spearman_r(a, b, dim, weights=weights, skipna=skipna)

    def spearman_r_p_value(self, a, b, dim, weights=None, skipna=False):
        a = self._in_ds(a)
        b = self._in_ds(b)
        return spearman_r_p_value(a, b, dim, weights=weights, skipna=skipna)

    def spearman_r_eff_p_value(self, a, b, dim, skipna=False):
        a = self._in_ds(a)
        b = self._in_ds(b)
        return spearman_r_eff_p_value(a, b, dim, skipna=skipna)

    def rmse(self, a, b, dim, weights=None, skipna=False):
        a = self._in_ds(a)
        b = self._in_ds(b)
        return rmse(a, b, dim, weights=weights, skipna=skipna)

    def mse(self, a, b, dim, weights=None, skipna=False):
        a = self._in_ds(a)
        b = self._in_ds(b)
        return mse(a, b, dim, weights=weights, skipna=skipna)

    def mae(self, a, b, dim, weights=None, skipna=False):
        a = self._in_ds(a)
        b = self._in_ds(b)
        return mae(a, b, dim, weights=weights, skipna=skipna)

    def median_absolute_error(self, a, b, dim, skipna=False):
        a = self._in_ds(a)
        b = self._in_ds(b)
        return median_absolute_error(a, b, dim, skipna=skipna)

    def mape(self, a, b, dim, weights=None, skipna=False):
        a = self._in_ds(a)
        b = self._in_ds(b)
        return mape(a, b, dim, weights=weights, skipna=skipna)

    def smape(self, a, b, dim, weights=None, skipna=False):
        a = self._in_ds(a)
        b = self._in_ds(b)
        return smape(a, b, dim, weights=weights, skipna=skipna)

    def crps_gaussian(self, observations, mu, sig, dim=None, weights=None):
        observations = self._in_ds(observations)
        mu = self._in_ds(mu)
        sig = self._in_ds(sig)
        return crps_gaussian(observations, mu, sig, dim=dim, weights=weights)

    def crps_ensemble(
        self,
        observations,
        forecasts,
        member_weights=None,
        issorted=False,
        dim=None,
        member_dim='member',
        weights=None,
    ):
        observations = self._in_ds(observations)
        forecasts = self._in_ds(forecasts)
        return crps_ensemble(
            observations,
            forecasts,
            member_weights=member_weights,
            issorted=issorted,
            member_dim=member_dim,
            dim=dim,
            weights=weights,
        )

    def crps_quadrature(
        self, x, cdf_or_dist, xmin=None, xmax=None, tol=1e-6, dim=None, weights=None
    ):
        x = self._in_ds(x)
        cdf_or_dist = self._in_ds(cdf_or_dist)
        return crps_quadrature(
            x, cdf_or_dist, xmin=xmin, xmax=xmax, tol=1e-6, dim=dim, weights=weights
        )

    def threshold_brier_score(
        self,
        observations,
        forecasts,
        threshold,
        issorted=False,
        dim=None,
        member_dim='member',
        weights=None,
    ):
        observations = self._in_ds(observations)
        forecasts = self._in_ds(forecasts)
        return threshold_brier_score(
            observations,
            forecasts,
            threshold,
            issorted=issorted,
            dim=dim,
            member_dim=member_dim,
            weights=weights,
        )

    def brier_score(self, observations, forecasts, dim=None, weights=None):
        observations = self._in_ds(observations)
        forecasts = self._in_ds(forecasts)
        return brier_score(observations, forecasts, dim=dim, weights=weights)
