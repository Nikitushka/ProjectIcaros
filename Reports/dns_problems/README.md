# The Problem
As mentioned in our [Wireguard-Client-Auto README](https://github.com/Nikitushka/ProjectIcaros/tree/main/Code/Wireguard-Client-Auto) we used a guide [by CK](https://www.ckn.io/blog/2017/11/14/wireguard-vpn-typical-setup/) to set up WireGuard on our server.

But for some reason, our VPN server refused to resolve hostnames to IP's, meaning that the DNS functionality refused to work. The problem lied in unbound, and starting it always resulted in the following errors:
```
sudo unbound-checkconf
  [1557921216] unbound-checkconf[5819:0] error: trust anchor presented twice
  [1557921216] unbound-checkconf[5819:0] error: could not parse auto-trust-anchor-file /var/lib/unbound/root.key line 2
  [1557921216] unbound-checkconf[5819:0] error: error reading auto-trust-anchor-file: /var/lib/unbound/root.key
  [1557921216] unbound-checkconf[5819:0] error: validator: error in trustanchors config
  [1557921216] unbound-checkconf[5819:0] error: validator: could not apply configuration settings.
  [1557921216] unbound-checkconf[5819:0] fatal error: bad config for validator module
```
After more than three hours of problem-solving and intense googling we found only ONE article that had a solution to this problem, even though countless people have experienced the same errors.

# The Solution

Turns out many articles on setting up a VPN server through WireGuard either forget to mention this, or perhaps it's a more recent problem, but a [WireGuard guide by Craig Hunter, written in May 2019](https://craighuther.com/2019/05/14/wireguard-setup-and-installation/) has a solution to these errors he [found through github](https://github.com/voxpupuli/puppet-unbound/issues/134#issuecomment-382287879).

And it's painfully simple:

Comment out a line in `/etc/unbound/unbound.conf` : `auto-trust-anchors-file config`

That's it. Nothing more. Hope this is of help to anyone who has the same problem.

# References 
[Wireguard-Client-Auto README](https://github.com/Nikitushka/ProjectIcaros/tree/main/Code/Wireguard-Client-Auto)

[ckn.io - WireGuard VPN: Typical Setup](https://www.ckn.io/blog/2017/11/14/wireguard-vpn-typical-setup/)

[Wireguard with Unbound DNS, server and client setup - Craig Hunter - 14 Mayb 2019](https://craighuther.com/2019/05/14/wireguard-setup-and-installation/)

[Github - fatal error: auto-trust-anchor-file: "/var/lib/unbound/root.key" does not exist in chrootdir /etc/unbound](https://github.com/voxpupuli/puppet-unbound/issues/134#issuecomment-382287879)
