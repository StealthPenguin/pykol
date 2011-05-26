import kol.Error as Error
from GenericRequest import GenericRequest
from kol.database import ItemDatabase
from kol.manager import PatternManager
from kol.util import StringUtils

class StoreInventoryRequest(GenericRequest):
        "This class is used to get a list of items currently in a user's store"

        def __init__(self, session):
                super(StoreInventoryRequest, self).__init__(session)
                self.url = session.serverURL + 'managestore.php'

	def parseResponse(self):
		firstSeparationPattern = PatternManager.getOrCompilePattern('firstSeparation')
		secondSeparationPattern = PatternManager.getOrCompilePattern('secondSeparation')

		items = []
		for item in firstSeparationPattern.finditer(self.responseText):
			name_quant = item.group(1) + ' (1)'
			for things in secondSeparationPattern.finditer(name_quant):
				name = things.group(1)
				amnt = things.group(2)
				m = {"item":name, "amnt":amnt}
				items.append(m)

		self.responseData["items"] = items
