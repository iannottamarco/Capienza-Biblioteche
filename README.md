# Capienza-Biblioteche
This python script fetches data about the number of people currently in Ca' Foscari's university libraries. This is all done thanks to the API, which does not need keys or authentication. The script runs every 5 minutes (refresh time of the API) and appends the new data to the one gathered so far. <p>
This is the structure of the pandas Dataframe generated: <p>
|   timestamp            |   biblioteca  |   persone  |   capienza  |
|------------------------|---------------|------------|-------------|
|   2023-11-01 17:54:28  |   CFZ         |   210      |   365       |
|   2023-11-01 17:54:28  |   BEC         |   122      |   280       |
|   2023-11-01 17:54:28  |   BAS         |   32       |   150       |
|   2023-11-01 17:54:28  |   BAUM        |   203      |   350       |
<p>
**timestamp:** timestamp when data was imported.
**biblioteca:** unique name of the library (distinct libraries are four).
**persone:** corresponds to the amount of people in the library at that exact timestamp.
**capienza:** is the maximum amount of available seats, it is static and does not change over time.

<p>
The script also generates a CSV file which is exported in the same directory.
