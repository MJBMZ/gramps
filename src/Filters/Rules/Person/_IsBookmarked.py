#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2002-2006  Donald N. Allingham
# Copyright (C) 2007       Brian Matherly
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

# $Id$

#-------------------------------------------------------------------------
#
# Standard Python modules
#
#-------------------------------------------------------------------------
from gettext import gettext as _

try:
    set()
except:
    from sets import Set as set
    
#-------------------------------------------------------------------------
#
# GRAMPS modules
#
#-------------------------------------------------------------------------
from Filters.Rules._Rule import Rule

#-------------------------------------------------------------------------
#
# IsBookmarked
#
#-------------------------------------------------------------------------
class IsBookmarked(Rule):
    """Rule that checks for the bookmark list in the database"""

    name        = _('Bookmarked people')
    category    = _('General filters')
    description = _("Matches the people on the bookmark list")

    def prepare(self,db):
        self.bookmarks = db.get_bookmarks().get()

    def apply(self,db,person):
        return person.handle in self.bookmarks
