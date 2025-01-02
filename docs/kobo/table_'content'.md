# Database Table Analysis: content

## Table Overview
- **Name:** content
- **Purpose:** This table records related information about a specific book 
- **Database:** sqlite

---

## Table Schema
| Column Name | Data Type | Nullable |
|-------------|-----------|----------|
| ContentID | TEXT | NOT NULL |
| ContentType | TEXT | NOT NULL |
| MimeType | TEXT | NOT NULL |
| BookID | TEXT | NULL |
| BookTitle | TEXT | NULL |
| ImageId | TEXT | NULL |
| Title | TEXT | NULL |
| COLLATE | NOCASE | NULL |
| Attribution | TEXT | NULL |
| COLLATE | NOCASE | NULL |
| Description | TEXT | NULL |
| DateCreated | TEXT | NULL |
| ShortCoverKey | TEXT | NULL |
| adobe_location | TEXT | NULL |
| Publisher | TEXT | NULL |
| IsEncrypted | BOOL | NULL |
| DateLastRead | TEXT | NULL |
| FirstTimeReading | BOOL | NULL |
| ChapterIDBookmarked | TEXT | NULL |
| ParagraphBookmarked | INTEGER | NULL |
| BookmarkWordOffset | INTEGER | NULL |
| NumShortcovers | INTEGER | NULL |
| VolumeIndex | INTEGER | NULL |
| ___NumPages | INTEGER | NULL |
| ReadStatus | INTEGER | NULL |
| ___SyncTime | TEXT | NULL |
| ___UserID | TEXT | NOT NULL |
| PublicationId | TEXT | NULL |
| ___FileOffset | INTEGER | NULL |
| ___FileSize | INTEGER | NULL |
| ___PercentRead | INTEGER | NULL |
| ___ExpirationStatus | INTEGER | NULL |
| FavouritesIndex | NOT | NULL |
| Accessibility | INTEGER | NULL |
| DEFAULT | 1 | NULL |
| ContentURL | TEXT | NULL |
| Language | TEXT | NULL |
| BookshelfTags | TEXT | NULL |
| IsDownloaded | BIT | NOT NULL |
| DEFAULT | 1 | NULL |
| FeedbackType | INTEGER | NULL |
| DEFAULT | 0 | NULL |
| AverageRating | INTEGER | NULL |
| DEFAULT | 0 | NULL |
| Depth | INTEGER | NULL |
| PageProgressDirection | TEXT | NULL |
| InWishlist | BOOL | NOT NULL |
| DEFAULT | FALSE | NULL |
| ISBN | TEXT | NULL |
| WishlistedDate | TEXT | NULL |
| FeedbackTypeSynced | INTEGER | NULL |
| DEFAULT | 0 | NULL |
| IsSocialEnabled | BOOL | NOT NULL |
| DEFAULT | TRUE | NULL |
| EpubType | INT | NOT NULL |
| Monetization | INTEGER | NULL |
| DEFAULT | 2 | NULL |
| ExternalId | TEXT | NULL |
| Series | TEXT | NULL |
| SeriesNumber | TEXT | NULL |
| Subtitle | TEXT | NULL |
| WordCount | INTEGER | NULL |
| Fallback | TEXT | NULL |
| RestOfBookEstimate | INTEGER | NULL | ⭐️
| CurrentChapterEstimate | INTEGER | NULL |
| CurrentChapterProgress | FLOAT | NULL |
| PocketStatus | INTEGER | NULL |
| DEFAULT | 0 | NULL |
| UnsyncedPocketChanges | TEXT | NULL |
| ImageUrl | TEXT | NULL |
| DateAdded | TEXT | NULL |
| WorkId | TEXT | NULL |
| Properties | TEXT | NULL |
| RenditionSpread | TEXT | NULL |
| RatingCount | INTEGER | NULL |
| DEFAULT | 0 | NULL |
| ReviewsSyncDate | TEXT | NULL |
| MediaOverlay | TEXT | NULL |
| MediaOverlayType | TEXT | NULL |
| RedirectPreviewUrl | TEXT | NULL |
| PreviewFileSize | INTEGER | NULL |
| EntitlementId | TEXT | NULL |
| CrossRevisionId | TEXT | NULL |
| DownloadUrl | TEXT | NULL |
| ReadStateSynced | BIT | NOT NULL |
| DEFAULT | false | NULL |
| TimesStartedReading | INTEGER | NULL |
| TimeSpentReading | INTEGER | NULL |
| LastTimeStartedReading | TEXT | NULL |
| LastTimeFinishedReading | TEXT | NULL |
| ApplicableSubscriptions | TEXT | NULL |
| ExternalIds | TEXT | NULL |
| PurchaseRevisionId | TEXT | NULL |
| SeriesID | TEXT | NULL |
| SeriesNumberFloat | REAL | NULL |
| AdobeLoanExpiration | TEXT | NULL |
| HideFromHomePage | bit | NULL |
| IsInternetArchive | BOOL | NOT NULL |
| DEFAULT | FALSE | NULL |
| titleKana | TEXT | NULL |
| subtitleKana | TEXT | NULL |
| seriesKana | TEXT | NULL |
| attributionKana | TEXT | NULL |
| publisherKana | TEXT | NULL |
| IsPurchaseable | BOOL | NULL |
| DEFAULT | TRUE | NULL |
| IsSupported | BOOL | NULL |
| DEFAULT | TRUE | NULL |
| AnnotationsSyncToken | TEXT | NULL |
| DateModified | TEXT | NULL |
| StorePages | INTEGER | NULL |
| DEFAULT | 0 | NULL |
| StoreWordCount | INTEGER | NULL |
| DEFAULT | 0 | NULL |
| StoreTimeToReadLowerEstimate | INTEGER | NULL |
| DEFAULT | 0 | NULL |
| StoreTimeToReadUpperEstimate | INTEGER | NULL |
| DEFAULT | 0 | NULL |
| Duration | INTEGER | NULL |
| DEFAULT | 0 | NULL |
| IsAbridged | BOOL | NULL |
| DEFAULT | NULL | NULL |
| SyncConflictType | INTEGER | NULL |
| DEFAULT | 0 | NULL |
| PRIMARY | KEY | NULL |

---

## Key Constraints
- **Primary Key:** [Column(s) that make up the primary key]
- **Foreign Keys:**
  - [Column Name] → [Referenced Table].[Referenced Column]
  - [Column Name] → [Referenced Table].[Referenced Column]
- **Unique Constraints:** [List of columns with unique constraints]

---

## Indexes
| Index Name       | Indexed Column(s)      | Type      | Description                     |
|------------------|------------------------|-----------|---------------------------------|
| [Index1 Name]    | [Column(s)]            | [Type]    | [Description]                  |
| [Index2 Name]    | [Column(s)]            | [Type]    | [Description]                  |

---

## Relationships
- **Parent Tables:** [Tables that this table references]
- **Child Tables:** [Tables that reference this table]

---

## Data Characteristics
- **Row Count:** [Approximate number of rows]
- **Data Volume:** [Size of the table, e.g., in GB]
- **Growth Rate:** [Estimated growth rate over time]

---

## Usage Patterns
- **Access Frequency:** [How often the table is accessed]
- **Primary Queries:** [Examples of common queries against this table]
- **Applications/Services:** [List of applications or services using this table]

---

## Observations and Recommendations
- **Performance Issues:** [Any identified performance bottlenecks]
- **Redundant Data:** [Any redundant or duplicate data observed]
- **Improvements:** [Suggestions for optimization or schema improvement]

---

## Notes
[Additional notes or observations about the table]