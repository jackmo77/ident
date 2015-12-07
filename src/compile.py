"""Aggregate the ident files for individual leagues in a year.

This aggregates the identification files for each league in a year into one file,
adding the appropriate path identifiers.  Entries are sorted by name
across all leagues.

Output is to _build/${year}-people.csv.  The _build directory is created if it
does not exist.
"""

import os
import glob

import pandas

if __name__ == '__main__':
    import sys
    year = sys.argv[1]

    dflist = [ ]
    for fn in glob.glob("%s/*/people.csv" % year):
        print "Reading %s" % fn
        df = pandas.read_csv(fn, encoding='utf-8')
        df['league.key'] = "%s/%s" % tuple(fn.split("/")[:2])
        df['person.key'] = df['league.key'] + "/" + df['person.key']
        dflist.append(df)

    df = pandas.concat(dflist, ignore_index=True)
    df.sort_values([ 'person.name.last', 'person.name.first', 'person.key' ],
                   inplace=True)

    df = df[[ 'league.key', 'person.key', 'person.name.last',
              'person.name.first', 'entry.name' ]]
    try:
        os.mkdir("_build")
    except IOError:
        pass

    print "Writing _build/%s-people.csv" % year
    df.to_csv("_build/%s-people.csv" % year,
              index=False, encoding='utf-8')
    print "All done"
                                                     
