#!/usr/bin/env python

print('cpu', '%s%% (user=%s, system=%s)' % (pinfo['cpu_percent'],
	getattr(pinfo['cpu_times'], 'user', '?'),
	getattr(pinfo['cpu_times'], 'system', '?')))
