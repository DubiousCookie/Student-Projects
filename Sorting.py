users = {'Hans' : 'active', 'Eleonore': 'inactive', 'KANJI' : 'active'}
active_users = {}
for user, status in users.items ():
    if status == 'active':
        active_users[user] = status; #use active_users to get the active users.

print(active_users); #using 'users' just gets KANJI????
print (users);
print (user);

