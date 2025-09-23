# MinIO Client (mc) Command Cheat Sheet

| Command Name               | Command Description                    | Example Usage                                                       |
| -------------------------- | -------------------------------------- | ------------------------------------------------------------------- |
| `mc alias set`             | Configure a new server alias           | `mc alias set myminio http://localhost:9000 minioadmin minioadmin`  |
| `mc alias list`            | List all configured server aliases     | `mc alias list`                                                     |
| `mc alias remove`          | Remove a server alias                  | `mc alias remove myminio`                                           |
| `mc ls`                    | List buckets and objects               | `mc ls myminio/`                                                    |
| `mc ls --recursive`        | List objects recursively               | `mc ls --recursive myminio/mybucket/`                               |
| `mc mb`                    | Create a new bucket                    | `mc mb myminio/newbucket`                                           |
| `mc rb`                    | Remove an empty bucket                 | `mc rb myminio/emptybucket`                                         |
| `mc rb --force`            | Remove bucket and all its contents     | `mc rb --force myminio/mybucket`                                    |
| `mc cp`                    | Copy files/objects                     | `mc cp file.txt myminio/mybucket/`                                  |
| `mc cp --recursive`        | Copy directories recursively           | `mc cp --recursive ./folder/ myminio/mybucket/`                     |
| `mc mv`                    | Move/rename files or objects           | `mc mv myminio/mybucket/old.txt myminio/mybucket/new.txt`           |
| `mc rm`                    | Remove objects                         | `mc rm myminio/mybucket/file.txt`                                   |
| `mc rm --recursive`        | Remove objects recursively             | `mc rm --recursive myminio/mybucket/folder/`                        |
| `mc rm --force`            | Remove objects without confirmation    | `mc rm --force myminio/mybucket/file.txt`                           |
| `mc mirror`                | Mirror files and folders               | `mc mirror ./local-folder/ myminio/mybucket/`                       |
| `mc mirror --watch`        | Continuously mirror with file watching | `mc mirror --watch ./local-folder/ myminio/mybucket/`               |
| `mc sync`                  | Synchronize files (one-way)            | `mc sync ./local-folder/ myminio/mybucket/`                         |
| `mc cat`                   | Display file contents                  | `mc cat myminio/mybucket/file.txt`                                  |
| `mc head`                  | Display first few lines of a file      | `mc head myminio/mybucket/file.txt`                                 |
| `mc tail`                  | Display last few lines of a file       | `mc tail myminio/mybucket/file.txt`                                 |
| `mc stat`                  | Display object metadata                | `mc stat myminio/mybucket/file.txt`                                 |
| `mc du`                    | Display disk usage                     | `mc du myminio/mybucket/`                                           |
| `mc find`                  | Find files and objects                 | `mc find myminio/mybucket/ --name "*.jpg"`                          |
| `mc find --larger`         | Find objects larger than size          | `mc find myminio/mybucket/ --larger 10MB`                           |
| `mc find --smaller`        | Find objects smaller than size         | `mc find myminio/mybucket/ --smaller 1MB`                           |
| `mc share download`        | Generate presigned download URL        | `mc share download myminio/mybucket/file.txt`                       |
| `mc share upload`          | Generate presigned upload URL          | `mc share upload myminio/mybucket/newfile.txt`                      |
| `mc share list`            | List active presigned URLs             | `mc share list download myminio/mybucket/`                          |
| `mc policy set`            | Set bucket policy                      | `mc policy set public myminio/mybucket`                             |
| `mc policy get`            | Get bucket policy                      | `mc policy get myminio/mybucket`                                    |
| `mc policy list`           | List all bucket policies               | `mc policy list myminio/`                                           |
| `mc policy set-json`       | Set custom policy from JSON file       | `mc policy set-json policy.json myminio/mybucket`                   |
| `mc version info`          | Show object version information        | `mc version info myminio/mybucket/file.txt`                         |
| `mc version enable`        | Enable versioning on bucket            | `mc version enable myminio/mybucket`                                |
| `mc version suspend`       | Suspend versioning on bucket           | `mc version suspend myminio/mybucket`                               |
| `mc encrypt set`           | Set bucket encryption                  | `mc encrypt set sse-s3 myminio/mybucket`                            |
| `mc encrypt info`          | Display encryption information         | `mc encrypt info myminio/mybucket`                                  |
| `mc encrypt clear`         | Clear bucket encryption                | `mc encrypt clear myminio/mybucket`                                 |
| `mc tag set`               | Set object tags                        | `mc tag set myminio/mybucket/file.txt "key1=value1&key2=value2"`    |
| `mc tag list`              | List object tags                       | `mc tag list myminio/mybucket/file.txt`                             |
| `mc tag remove`            | Remove object tags                     | `mc tag remove myminio/mybucket/file.txt`                           |
| `mc ilm add`               | Add lifecycle management rule          | `mc ilm add --expiry-days 30 myminio/mybucket`                      |
| `mc ilm ls`                | List lifecycle rules                   | `mc ilm ls myminio/mybucket`                                        |
| `mc ilm rm`                | Remove lifecycle rule                  | `mc ilm rm --id "rule1" myminio/mybucket`                           |
| `mc admin info`            | Display server information             | `mc admin info myminio`                                             |
| `mc admin service restart` | Restart MinIO service                  | `mc admin service restart myminio`                                  |
| `mc admin user add`        | Add new user                           | `mc admin user add myminio newuser newpassword`                     |
| `mc admin user list`       | List all users                         | `mc admin user list myminio`                                        |
| `mc admin user remove`     | Remove user                            | `mc admin user remove myminio username`                             |
| `mc admin group add`       | Add user to group                      | `mc admin group add myminio developers user1 user2`                 |
| `mc admin policy add`      | Add custom policy                      | `mc admin policy add myminio mypolicy policy.json`                  |
| `mc admin policy list`     | List all policies                      | `mc admin policy list myminio`                                      |
| `mc admin policy attach`   | Attach policy to user/group            | `mc admin policy attach myminio mypolicy --user username`           |
| `mc watch`                 | Watch for file system events           | `mc watch myminio/mybucket/`                                        |
| `mc event add`             | Add bucket event notification          | `mc event add myminio/mybucket arn:aws:sqs::1:webhook --event put`  |
| `mc event list`            | List bucket event notifications        | `mc event list myminio/mybucket`                                    |
| `mc event remove`          | Remove bucket event notification       | `mc event remove myminio/mybucket arn:aws:sqs::1:webhook`           |
| `mc sql`                   | Run SQL queries on objects             | `mc sql --query "select * from s3object" myminio/mybucket/data.csv` |

## Common Flags

| Flag           | Description                            |
| -------------- | -------------------------------------- |
| `--recursive`  | Apply command recursively              |
| `--force`      | Force operation without confirmation   |
| `--json`       | Output in JSON format                  |
| `--quiet`      | Suppress output                        |
| `--continue`   | Continue interrupted operations        |
| `--exclude`    | Exclude files matching pattern         |
| `--include`    | Include only files matching pattern    |
| `--older-than` | Select files older than specified time |
| `--newer-than` | Select files newer than specified time |

## Configuration Files

- **Config Location**: `~/.mc/config.json`
- **Session Location**: `~/.mc/session/`
- **Cache Location**: `~/.mc/cache/`