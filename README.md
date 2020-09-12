# Tag Panda

Discord bot to allow guild members to manage their own content related tags (i.e roles, though we don't use that term).

Needs a bot token exported as `DISCORD_TOKEN` and sufficiant permissions on-server.

Write the Pipfile via the Makefile (keeps everything in sync, i.e avoids pulling any hardware dependencies in). Som add any new dependencies to the Pipfile, then it's literally just `Make` to lock it using the on-server environment.