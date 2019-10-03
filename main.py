import json
import logging
import requests
import glob
import ntpath
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.action.OpenAction import OpenAction
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem

logger = logging.getLogger(__name__)

class PedroTrollerWorkspaceExtension(Extension):

    def __init__(self):
        super(PedroTrollerWorkspaceExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        query = event.get_argument()

        logger.debug(query);

        if not query:
            return;

        items = []

        for workspace in glob.glob('/home/pedro/Works/*'):
            name = ntpath.basename(workspace)

            if query.lower() in name.lower():
                items.append(ExtensionResultItem(
                    name=name,
                    description=workspace,
                    icon='images/work.png',
                    on_enter=OpenAction(workspace)
                ))

        for project in glob.glob('/home/pedro/Works/*/*'):
            name = ntpath.basename(project)

            if query.lower() in name.lower():
                items.append(ExtensionResultItem(
                    name=name,
                    description=project,
                    icon='images/work.png',
                    on_enter=OpenAction(project)
                ))

        return RenderResultListAction(items)

if __name__ == '__main__':
    PedroTrollerWorkspaceExtension().run()
