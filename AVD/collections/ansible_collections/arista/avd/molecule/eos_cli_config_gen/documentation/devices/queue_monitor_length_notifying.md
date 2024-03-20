# queue_monitor_length_notifying

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Queue Monitor](#queue-monitor)
  - [Queue Monitor Length](#queue-monitor-length)
  - [Queue Monitor Configuration](#queue-monitor-configuration)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | MGMT | 10.73.255.122/24 | 10.73.255.2 |

##### IPv6

| Management Interface | description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management1 | oob_management | oob | MGMT | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management1
   description oob_management
   vrf MGMT
   ip address 10.73.255.122/24
```

## Queue Monitor

### Queue Monitor Length

| Setting | Value |
| ------- | ----- |
| Enabled | True
| Logging Interval | - |
| Default Thresholds High | 100 |
| Default Thresholds Low | - |
| Notifying | disabled |
| TX Latency | disabled |
| CPU Thresholds High | - |
| CPU Thresholds Low | - |

### Queue Monitor Configuration

```eos
!
queue-monitor length
queue-monitor length default threshold 100
no queue-monitor length notifying
```
