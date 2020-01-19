# Using EnOS Device SDK for Python
Table of Contents

* [Installation](#install)
    * [Prerequisites](#pre)
    * [Installing from Pip](#pip)
    * [Building From Source](#obtaining)
* [Feature List](#feature)
* [Quick Start](#start)
* [Sample Codes](#sample)
* [Related Information](#information)
* [Release Notes](#releasenotes)



The EnOS Device SDK for Python allows developers to write Python scripts to use their devices to access EnOS IoT hub through MQTT.

<a name="install"></a>

## Installation

<a name="pre"></a>

### Prerequisites

To use the EnOS Device SDK, you will need  Python 3.5.3 or later, and `pip` is required. Note that Python 2.x is not recommended as some functions might not be compatible with Python 2.x in future SDK versions.

If you are upgrading from an earlier version of EnOS Device SDK for Python, you need to change the path of the SDK package by adding `enos` prefix in your "Import" statement  in the existing Python codes to use the latest version.

You can install the SDK from pip, or build from source.

<a name="pip"></a>

### Installing from pip

The latest version of EnOS Device SDK for Python is available in the Python Package Index (PyPi) and can be installed using

```bash 
pip install enos-mqtt-sdk-python
```
Update `setuptools` if necessary:

```bash
pip install --upgrade setuptools
```

<a name="obtain"></a>

### Building From Source

1. Obtain the source code of EnOS Device SDK for Python.
   - From GitHub:
    ```
    git clone https://github.com/EnvisionIot/enos-mqtt-sdk-python.git
    ```
   - From EnOS SDK Center. Click **SDK Center** from the left navigation of EnOS Console, and obtain the SDK source code by clicking the GitHub icon in the **Obtain** column.


2. From the directory where the source code is stored, run the following command:

   ```
   python setup.py install
   ```
   


<a name="feature"></a>

## Feature List

For the list of features supported by this SDK and the availability of EnOS device connectivity and management features in all SDKs we provide, see [EnOS Device SDK](https://github.com/EnvisionIot/enos-iot-device-sdk).


<a name="start"></a>

## Quick Start

1. Create an MQTT client and connect it to EnOS Cloud using the secret-per-device authentication:

```python
client = MqttClient(enos_mqtt_url, product_key, device_key, device_secret)
client.connect()
```
2. Build a request to post a measurement point and publish the request using the connected client.

```py
measure_point_post_request = MeasurepointPostRequest.builder() 
    .add_measurepoint('measurepoint_id', measurepoint_value) 
    .set_timestamp(timestamp) 
    .build()
# publish request and wait for the response
measure_point_response = client.publish(measure_point_post_request)
```
3. Close the connection

```python
client.close()
```

<a name="sample"></a>

## Sample Codes
* [Establishing Connection with EnOS Cloud](/enos/sample/ConnectionSample.py)
* [Device Tag Operations](/enos/sample/TagSample.py)
* [Device Attribute Operations](/enos/sample/AttributeSample.py)
* [Reporting Measurement Points](/enos/sample/MeasurepointPostSample.py)
* [Reporting Events](/enos/sample/EventSample.py)
* [Receiving Commands from Cloud](/enos/sample/CommandSample.py)
* [Passing Through Device Information or Receiving Passed-through Information from Cloud](/enos/sample/ModelUpRawSample.py)
* [Managing Sub-devices](/enos/sample/SubDeviceSample.py)

<a name="information"></a>

## Related Information
* To learn more about EnOS IoT Hub, see [EnOS IoT Hub Documentation](https://support.envisioniot.com/docs/device-connection/en/latest/device_management_overview.html).
* To learn more about how to develop your device for EnOS IoT Hub, see EnOS Device Development Guide (Python).

<a name="releasenotes"></a>

## Release Notes
- 2019/11/15(0.1.0): Reconstruction and new functions added.