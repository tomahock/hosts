# Hosts #
A curated list of hosts to use when the internet is broken!

## Why? ##

You know what to blame when something is broken! *D*omain *N*ame *S*ystem or what you probably know as *DNS*! You also probably hear about some [DDoS](https://krebsonsecurity.com/2016/08/inside-the-attack-that-almost-broke-the-internet/) [DNS](https://business.kaspersky.com/root-servers-ddos/4978/) [Attacks](https://krebsonsecurity.com/2016/10/ddos-on-dyn-impacts-twitter-spotify-reddit/).

## How? ##
I have my own [pi-hole](https://pi-hole.net) instance that uses [dnsmasq](http://www.thekelleys.org.uk/dnsmasq/doc.html). All my devices are configured to have their nameservers pointed to my pi-hole. Dnsmasq allows to have extra hosts files. So on my rPi I have this repo with a cronjob that refreshes this hosts list and commits to this repo! You can get your own rPi running pi-hole and add this host file by just adding it on the dnsmasq config!
You can also just copy paste to `/etc/hosts` :)

## Domains ##
The domain list it's a personal list of must have ips! If you want to have another domain here just Pull Request the domain.txt!

---
## License ##

This software is released under the MIT License.

Copyright (C) 2016 João Pina

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

