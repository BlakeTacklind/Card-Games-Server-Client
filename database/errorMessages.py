
class ERROR:
	badJSON={'error':-1}
	noRQ={'error':-5}
	noAG={'error':-6}
	badTypeRQ={'error':-10}
	badTypeAG={'error':-11}

	def missingARG(rq, arg):
		return {'error':-50, 'request': rq, 'argument': arg}

	def badTypeARG(rq, arg):
		return {'error':-55, 'request': rq, 'argument': arg}

	def InvalidCharARG(rq, arg):
		return {'error':-100, 'request': rq, 'argument': arg}

