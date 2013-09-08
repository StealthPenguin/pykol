import kol.Error as Error
from GenericRequest import GenericRequest

class TakeItemsFromStoreRequest(GenericRequest):
    "Removes all of one item from the player's store"

    def __init__(self, session, itemId):
        super(TakeItemsFromStoreRequest, self).__init__(session)
        self.url = session.serverURL + 'managestore.php'
        self.requestData['action'] = "takeall"
        self.requestData['whichitem'] = itemId
