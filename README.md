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
Tested with Ubuntu 14.04 

```
apt-get install libyaml-dev firefox xvfb
pip install -r requirements.txt
python setup.py install
```


References
----------
- https://developer.mozilla.org/en-US/docs/Web/API/PerformanceTiming
- https://developer.mozilla.org/en/docs/Web/API/Navigation_timing_API


Author
------
* Alok Jani 
