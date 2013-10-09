# To run automated tests, $ python db.py -v 
# At the moment, the test depends on test data in the DB. 

class SafetyDB(object):
    def __init__(self):
        """
        Create a connection to the Safety DB

        >>> db = SafetyDB()
        >>> rt = db.checkUrl( "http://curtis.lassam.net" )
        >>> print rt["status"]
        SAFE
        >>> print rt["url"]
        http://curtis.lassam.net
        >>> db.close()
        """
        import cql
        # TODO: tie these to an external config 
        host = 'localhost'
        port = 9160
        keyspace = 'duke'

        self.connection = cql.connect(host, port, keyspace, cql_version='3.0.0')
        self.cursor = self.connection.cursor()

    def checkUrl(self, url):
        """ Return an object 
                {'url':'http://example.org', 
                 'status':'SAFE', 
                 'reason':'long description' }
            Or, if not found
                {'url':'http://notfound.bad', 
                 'status':'UNKN', 
                 'reason':'not found' }
            Current statuses: 
                'SAFE', 'WARN', 'UNKN', 'NOPE' 
        """
        
        return_obj = {'url': url, 'status':'UNKN', 'reason':'URL not found.' }
        self.cursor.execute("SELECT url, status, reason FROM safety_dance WHERE url=:url;", 
                        {'url':url} )
        for row in self.cursor:
            return_obj['status'] = row[1]
            return_obj['reason'] = row[2]
            return return_obj
        return return_obj

    def close(self):
        self.cursor.close()
        self.connection.close()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
