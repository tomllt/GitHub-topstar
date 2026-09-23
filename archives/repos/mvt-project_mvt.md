<p align="center">
     <img src="https://docs.mvt.re/en/latest/mvt.png" width="200" />
</p>

# Mobile Verification Toolkit

> [!IMPORTANT]
> We recently merged the "v3" branch. This introduced breaking changes. If you relied on mvt output in other scripts They might have broken. More details: https://github.com/mvt-project/mvt/issues/757

[![](https://img.shields.io/pypi/v/mvt)](https://pypi.org/project/mvt/)
[![Documentation Status](https://readthedocs.org/projects/mvt/badge/?version=latest)](https://docs.mvt.re/en/latest/?badge=latest)
[![CI](https://github.com/mvt-project/mvt/actions/workflows/tests.yml/badge.svg)](https://github.com/mvt-project/mvt/actions/workflows/tests.yml)
[![Downloads](https://pepy.tech/badge/mvt)](https://pepy.tech/project/mvt)

Mobile Verification Toolkit (MVT) is a collection of utilities to simplify and automate the process of gathering forensic traces helpful to identify a potential compromise of Android and iOS devices.

It has been developed and released by the [Amnesty International Security Lab](https://securitylab.amnesty.org) in July 2021 in the context of the [Pegasus Project](https://forbiddenstories.org/about-the-pegasus-project/) along with [a technical forensic methodology](https://www.amnesty.org/en/latest/research/2021/07/forensic-methodology-report-how-to-catch-nso-groups-pegasus/). It continues to be maintained by Amnesty International and other contributors.

> **Note**
> MVT is a forensic research tool intended for technologists and investigators. It requires understanding digital forensics and using command-line tools. This is not intended for end-user self-assessment. If you are concerned with the security of your device please seek reputable expert assistance.
>

### Indicators of Compromise

MVT supports using public [indicators of compromise (IOCs)](https://github.com/mvt-project/mvt-indicators) to scan mobile devices for potential traces of targeting or infection by known spyware campaigns. This includes IOCs pu

... (truncated)