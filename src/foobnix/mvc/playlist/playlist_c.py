'''
Created on Mar 11, 2010

@author: ivan
'''

import gtk
from foobnix.song import Song
from foobnix.mvc.playlist.playlist_m import PlaylistModel
from foobnix.mvc.model.entity import PlaylistBean
from foobnix.mouse_utils import is_double_click

class PlaylistCntr():
    def __init__(self, widget, playerCntr):
        self.model = PlaylistModel(widget)
        self.playerCntr = playerCntr
        self.model.append(PlaylistBean(gtk.STOCK_GO_FORWARD, "1", "Description", "path", "#F2F2F2"))
        self.model.append(PlaylistBean(None, "12", "Description", "path", "#FFFFE5"))
        widget.connect("button-press-event", self.onPlaySong)
        
        self.entityBeans = []
        self.index = 0;
        
    def clear(self):
        self.model.clear()
        
    def onPlaySong(self, w, e):
        if is_double_click(e):
            playlistBean = self.model.getSelectedBean()           
            self.repopulate(self.entityBeans, playlistBean.index);
            self.index = playlistBean.index
            self.playerCntr.playSong(playlistBean)
            
    def getNextSong(self):
        self.index += 1
        if self.index >= len(self.entityBeans):
            self.index = 0
            
        playlistBean = self.model.getBeenByPosition(self.index)           
        self.repopulate(self.entityBeans, playlistBean.index);        
        return playlistBean
        
     
    def setPlaylist(self, entityBeans):
        self.entityBeans = entityBeans    
        index = 0
        if entityBeans:
            self.playerCntr.playSong(entityBeans[index])
            self.repopulate(entityBeans, index);
        
    def repopulate(self, entityBeans, index):
        self.model.clear()        
        for i in range(len(entityBeans)):
            songBean = entityBeans[i]            
            color = self.getBackgroundColour(i)
            
            if i == index:                
                self.model.append(PlaylistBean(gtk.STOCK_GO_FORWARD, songBean.tracknumber, songBean.name, songBean.path, color, i))
            else:
                self.model.append(PlaylistBean(None, songBean.tracknumber, songBean.name, songBean.path, color, i))
                   
    def getBackgroundColour(self, i):
        if i % 2 :
            return "#F2F2F2"
        else:
            return "#FFFFE5"