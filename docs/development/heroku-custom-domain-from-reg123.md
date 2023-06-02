---
title: "Using custom domain from Reg123 on heroku"
tags: webdev, hosting, DNS
author: Colm Britton
---

I wanted to use a domain I own for a small python app running on [heroku](https://www.heroku.com/home).

Instead of using `myapp.herokuapp.com`, I wanted people to use `mydomain.com` to visit the site.

It was easy to set up from the heroklu side but it was trickier to sort out the DNS settings on my domain name provider, [Reg123](https://www.123-reg.co.uk).

I was able to set up the `www` domain easily enough by setting the `www` `CNAME` to the server heroku provides under **app > settings > domains > DNS target**.

However I did know how to set up the root or "blank" domain. I learnt that is what you call the domain without `www.` in front of it.

When creating DNS records for blank domains they are often labelled/named using the `@` symbol.

On Reg123 I didn't seem to be able to set the `CNAME` record for `@` - whatever I put in there it froze.

I stumbled upon the solution by adding an `@` `A` DNS record. `A` records expect the target to be an IP address not a URL.

I found the IP address for the heroku DNS target using the `ping` command in the terminal. Run

    ping <name-of-server>.herokudns.com

This will return something similar to

    PING <name-of-server>.herokudns.com (192.188.12.12): 56 data bytes

You are looking for the XXX.XXX.XX.XX bit. Copy and paste that into the `A` record for the `@` domain.

I ended up with a set of DNS records in Reg123 that looked like this.

![Screenshot of the DNS records set for a domain on Reg123. Shows the @ A record set to the IP I found from pinging heroku](/static/images/notes/webdev/reg123-dns-record-example.png)
