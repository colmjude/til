title: "Read SQL into dataframe"
tags: webdev, python, flask, development, sqlite, database, pandas
author: Colm Britton
--------------------

The key line is:

    pd.read_sql(query.statement, db.engine, index_col="date")

[`read_sql()` docs](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_sql.html)

### Things I learnt

Needs db engine. Using Flask SQLAlchemy you can access the engine with 

    db.engine

Expects a SQL string. Not how do things in FlaskSQLAlchemy, don't write your own SQL, compose queries. E.g.

    PriceData.query.filter_by(symbol="AAPL", interval="day").filter(
            PriceData.date.between("2021-03-01", "2021-04-08")

But you can get the SQL by tacking `statement` on the end of the query object. E.g.

    sql = PriceData.query.filter_by(symbol="AAPL", interval="day").filter(
            PriceData.date.between("2021-03-01", "2021-04-08").statement

or

    query = PriceData.query.filter_by(symbol="AAPL", interval="day").filter(
            PriceData.date.between("2021-03-01", "2021-04-08")
    sql = query.statement