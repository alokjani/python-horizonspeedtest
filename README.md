OpenStack Horizon SpeedTest
===========================
Measures page load times for OpenStack's Horizon UI with Firefox.


Description
-----------
Useful when making dashboard customizations or checking the effect of different
OpenStack SDN/storage backends from end UX perspective.

Uses Python, Selenium and the Mozilla PerformanceTiming interface (see references)


Install
-------

```
apt-get install git python-pip python-dev libyaml-dev firefox xvfb
pip install -r requirements.txt
python setup.py install
```
Tested with Ubuntu 14.04


References
----------
- https://developer.mozilla.org/en-US/docs/Web/API/PerformanceTiming
- https://developer.mozilla.org/en/docs/Web/API/Navigation_timing_API


Author
------
* Alok Jani 
