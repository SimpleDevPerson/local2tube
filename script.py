import curses
import os
from ytmusicapi import YTMusic

ytmusic = YTMusic("oauth.json")



filenames = os.listdir("Music")
id_add_list = []
songs_add_list = []

def main():

    if "playlistid.txt" in str(os.listdir(".")):
        playlist_id = open("playlistid.txt", "r").readline()
        print("Found playlist id" + playlist_id + " in current directory, proceeding")
    else:
        print("You can find your playlist id at the end of the playlist url, after list=")
        playlist_id = input("Enter playlist id: ")
    
    oScreen = curses.initscr()
    curses.noecho()
    curses.curs_set(0)
    oScreen.keypad(1)
    oScreen.scrollok(1)
    oScreen.idlok(True)

    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(3, curses.COLOR_GREEN, 0)
    curses.init_pair(4, curses.COLOR_RED, 0)

    song_number = 0

    for filename in filenames:
        if not filename.endswith(".lrc") and not filename.endswith(".txt"):
            song_number += 1
            total_songs = len(filenames)
            search_results = ytmusic.search(query=filename, filter="songs", limit=1)
            f = open("risultato.txt", "w")
            f.write(str(search_results).encode("cp1252", errors="replace").decode("cp1252"))
            f.close()


            oScreen.addstr("File: " + "\n", curses.color_pair(1))
            oScreen.addstr(filename + "\n")
            oScreen.addstr("\n")
            oScreen.addstr("Match: "  "\n", curses.color_pair(2))
            info = search_results[0]["title"] + " - " + search_results[0]["artists"][0]["name"]
            oScreen.addstr(info + "\n")
            oScreen.addstr("\n")
            oScreen.addstr("Add it to the playlist?\n\n", curses.A_BOLD)
            oScreen.addstr("\t" + "y", curses.color_pair(3))
            oScreen.addstr("/", curses.A_BOLD)
            oScreen.addstr("n" + "\n", curses.color_pair(4))
            oScreen.addstr("\n")
            oScreen.addstr("Song number: " + str(song_number) + "/" + str(total_songs) + "\n")
            song_string = str(songs_add_list).encode("cp1252", errors="replace").decode("cp1252")
            oScreen.addstr("Added songs:" + "\n" + str(songs_add_list).encode("cp1252", errors="replace").decode("cp1252")[len(str(songs_add_list)) - 100:] + "\n")
            
            oEvent = oScreen.getch()
            if oEvent == ord("y"):
                id_add_list.append(search_results[0]["videoId"])
                songs_add_list.append(info)
                os.rename("Music/" + filename, "Out/" + filename)
                oScreen.addstr("Added!\n\n")
                oScreen.clear()
                oScreen.refresh()
            elif oEvent == ord("n"):
                oScreen.addstr("Not added!\n")
                oScreen.clear()
                oScreen.refresh()
            else:
                pass
                

        else:
            pass


    try:
        ytmusic.add_playlist_items(playlistId=playlist_id, videoIds=id_add_list, duplicates=False)
        print("Done!")
        exit()
    except Exception:
        print("Error :(")

    curses.endwin()


if __name__ == "__main__":
    main()