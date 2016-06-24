# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016 CERN.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Remote account dump functions."""

from __future__ import absolute_import, print_function


def get(*args, **kwargs):
    """Get users."""
    from invenio.modules.oauthclient.models import RemoteAccount
    q = RemoteAccount.query
    return q.count(), q.all()


def dump(ra, from_date, with_json=True, latest_only=False, **kwargs):
    """Dump the remote accounts as a list of dictionaries.

    :param ra: Remote account to be dumped.
    :type ra: `invenio_oauthclient.models.RemoteAccount [Invenio2.x]`
    :returns: Remote accounts serialized to dictionary.
    :rtype: dict
    """
    return dict(id=ra.id, user_id=ra.user_id, client_id=ra.client_id,
                extra_data=ra.extra_data)
