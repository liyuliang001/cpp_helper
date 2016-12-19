import sys
def firstToUpper(s):
	return s[0].upper() + s[1:].lower()
if __name__ == "__main__":
	if len(sys.argv) != 2:
		print "usage: python cpp_class_gen.py <class_name>"
		sys.exit(0)
	name = sys.argv[1]
	tokens = name.split('_')
	
	cpp = open("%s.cpp"%name,"w")
	cpp.write('#include "%s.hpp"'%name)
	cpp.close()

	macro = "_".join(map(lambda x: x.upper(), tokens)) + "_HPP"
	classname = "".join(map(firstToUpper, tokens))
	
	hpp = open("%s.hpp"%name, "w")
	hpp.write("#ifndef %s\n"%macro)
	hpp.write("#define %s\n"%macro)
	hpp.write("class %s{\n"%classname)
	hpp.write("}; /* class %s */\n"%classname)
	hpp.write("#endif /* %s */"%macro)
	hpp.close()
