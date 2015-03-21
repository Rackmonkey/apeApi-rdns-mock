# apeControl Reverse DNS Api
This api is modelled after the [hetzner rdns api][1].

## Routes

### /rdns

#### [GET]
Returns an array of all set rdns records.

##### Example Response
```javascript
[
  {
  "rdns": {
    "ip": "123.123.123.123",
    "ptr": "testen.de"
  }
 },
 {
  "rdns": {
    "ip": "124.124.124.124",
    "ptr": "your-server.de"
  }
 }
]
```

##### Error Codes
| Status | Code                         |
|--------|------------------------------|
| 404    | NOT_FOUND                    |


### /rdns/:ip

#### [GET]
Returns the current set rdns record.

##### Example Response
```javascript
{
  "rdns": {
  "ip": "123.123.123.123",
  "ptr": "testen.de"
 }
}
```

##### Error Codes
| Status | Code                         |
|--------|------------------------------|
| 404    | IP_NOT_FOUND                 |
| 404    | RDNS_NOT_FOUND               |

#### [POST] / [PUT]
Set or update a rdns record.

##### Example Request
```javascript
{
  "rdns": {
  "ip": "123.123.123.123",
  "ptr": "testen.de"
 }
}
```

##### Error Codes
| Status | Code                         |
|--------|------------------------------|
| 404    | IP_NOT_FOUND                 |
| 404    | RDNS_NOT_FOUND               |
| 500    | RDNS_CREATE_FAILED           |
| 500    | RDNS_UPDATE_FAILED           |

#### [DELETE]
Deletes the rdns record.

##### Error Codes
| Status | Code                         |
|--------|------------------------------|
| 404    | IP_NOT_FOUND                 |
| 500    | RDNS_DELETE_FAILED           |

[1]: http://wiki.hetzner.de/index.php/Robot_Webservice#Reverse_DNS

