# SQLite Music

## Questions

2.1. ArtistID in the table Album acts as a reference to a row in a different table, the row and primary key ArtistID in the table Artist.

2.2. A relationship between the tables Album and Artist was already established by the presence of the foreign key ArtistID in Album
from Artist. Further, while every AlbumID in Album had a single ArtistID corresponding to it, a ArtistID in Artist can have multiple
AlbumID values associated with it, since an artist may have had multiple albums, which is an inefficiency that it is better to avoid.

2.3. While the customer's given ID number won't ever change, his email address can, which would require that a primary key value be
changed, which is a massive change to the table. Additionally, if needed, it is faster to retrieve data using an integer value than a text value and, if
the primary key needs to be used as a foreign key in a different table and thus take up space there, it is more efficient to have an integer
as a primary key because integer values take up less storage space than a text value.

2.4. SELECT SUM(Total) FROM Invoice WHERE InvoiceDate BETWEEN "2010-01-01 00:00:00" AND "2010-12-31 23:59:59";

2.5. SELECT Name FROM Track WHERE TrackId IN (SELECT TrackId FROM InvoiceLine WHERE InvoiceId IN (SELECT InvoiceId FROM Invoice WHERE CustomerId = 50));

2.6. The column Composer can be removed from table Track and two new tables, Composer and ComposerTrack, can be made, with Composer
having columns "Name", under which is listed all the names of the individual composers, with the column being of type TEXT,
and a column called "ComposerId" to serve as a primary key, being of an integer value and with each row having a unique integer value,
and with ComposerTrack having the foreign keys ComposerId and TrackId, with each allowed to be repeated in order to portray
what composers were behind each track (i.e. in different rows, the same ComposerId will take associate with different TrackId's to represent
all the tracks the composer aided in composing). The need for two tables is, in a situation similar to how the tables Playlist and PLaylistTrack both exist,
to avoid having to list any name of a composer more than once, as it takes less space to repeatedly store an integer value like ComposerId than to repeatedly store a text value like Name.

## Debrief

a. https://www.tutorialspoint.com/sql/sql-sub-queries.html, Lecture 10 notes

b. 60 minutes
