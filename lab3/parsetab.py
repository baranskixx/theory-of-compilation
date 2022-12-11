
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocIFnonassocELSErightMULASSIGNDIVASSIGNSUBASSIGNADDASSIGNnonassoc<>GEQLEQEQNEQleft+-leftDOTADDDOTSUBleft*/leftDOTMULDOTDIVrightUMINUSleft\'ADDASSIGN BREAK CONTINUE DIVASSIGN DOTADD DOTDIV DOTMUL DOTSUB ELSE EQ EYE FLOAT FOR GEQ ID IF INTNUM LEQ MULASSIGN NEQ ONES PRINT RETURN STRING SUBASSIGN WHILE ZEROSstart :\n            | instructions instructions : instr\n                    | instructions instr instr : instr_if\n                | instr_for\n                | instr_while\n                | instr_return \';\'\n                | instr_assign \';\'\n                | instr_print \';\'\n                | break \';\'\n                | continue \';\'  instr : \'{\' instructions \'}\'  instr_if : IF \'(\' expr \')\' instr %prec IF\n                    | IF \'(\' expr \')\' instr ELSE instr instr_return : RETURN\n                        | RETURN expr instr_for : FOR id \'=\' expr \':\' expr instr instr_while : WHILE \'(\' expr \')\' instrbreak : BREAKcontinue : CONTINUEstr : STRING instr_print : PRINT printables printables : printable\n                | printables \',\' printable printable : expr\n                | str instr_assign : assignable \'=\' expr\n                    | assignable ADDASSIGN expr\n                    | assignable SUBASSIGN expr\n                    | assignable MULASSIGN expr\n                    | assignable DIVASSIGN exprid : ID assignable : id\n                    | matrix_element\n                    | vector_elementexpr : expr \'\\\'\'expr : \'(\' expr \')\' expr : matrix_create \'(\' expr \')\'expr : "-" expr %prec UMINUSexpr : assignable\n            | matrixexpr : INTNUMexpr : FLOATexpr : expr \'+\' expr\n            | expr \'-\' expr\n            | expr \'*\' expr\n            | expr \'/\' expr\n            | expr DOTADD expr\n            | expr DOTSUB expr\n            | expr DOTMUL expr\n            | expr DOTDIV expr\n            | expr \'>\' expr\n            | expr \'<\' expr\n            | expr EQ expr\n            | expr NEQ expr\n            | expr LEQ expr\n            | expr GEQ expr \n             matrix : \'[\' vectors \']\' matrix_create : ZEROS\n                            | ONES\n                            | EYE matrix_element : id "[" INTNUM "," INTNUM "]" vectors : vectors \',\' vector\n               | vector vector : \'[\' variables \']\'  vector_element : id "[" INTNUM "]" variables : variables \',\' variable\n                 | variable variable : INTNUM\n                | FLOAT\n                | assignable '
    
_lr_action_items = {'$end':([0,1,2,3,4,5,6,25,26,27,28,29,30,58,119,122,131,132,],[-1,0,-2,-3,-5,-6,-7,-4,-8,-9,-10,-11,-12,-13,-14,-19,-15,-18,]),'{':([0,2,3,4,5,6,12,15,22,23,24,25,26,27,28,29,30,31,40,41,42,43,58,63,80,90,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,116,119,122,123,127,128,129,131,132,],[12,12,-3,-5,-6,-7,12,-34,-35,-36,-33,-4,-8,-9,-10,-11,-12,12,-41,-42,-43,-44,-13,-37,-40,12,-67,12,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-38,-59,-14,-19,-39,12,12,-63,-15,-18,]),'IF':([0,2,3,4,5,6,12,15,22,23,24,25,26,27,28,29,30,31,40,41,42,43,58,63,80,90,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,116,119,122,123,127,128,129,131,132,],[13,13,-3,-5,-6,-7,13,-34,-35,-36,-33,-4,-8,-9,-10,-11,-12,13,-41,-42,-43,-44,-13,-37,-40,13,-67,13,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-38,-59,-14,-19,-39,13,13,-63,-15,-18,]),'FOR':([0,2,3,4,5,6,12,15,22,23,24,25,26,27,28,29,30,31,40,41,42,43,58,63,80,90,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,116,119,122,123,127,128,129,131,132,],[14,14,-3,-5,-6,-7,14,-34,-35,-36,-33,-4,-8,-9,-10,-11,-12,14,-41,-42,-43,-44,-13,-37,-40,14,-67,14,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-38,-59,-14,-19,-39,14,14,-63,-15,-18,]),'WHILE':([0,2,3,4,5,6,12,15,22,23,24,25,26,27,28,29,30,31,40,41,42,43,58,63,80,90,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,116,119,122,123,127,128,129,131,132,],[16,16,-3,-5,-6,-7,16,-34,-35,-36,-33,-4,-8,-9,-10,-11,-12,16,-41,-42,-43,-44,-13,-37,-40,16,-67,16,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-38,-59,-14,-19,-39,16,16,-63,-15,-18,]),'RETURN':([0,2,3,4,5,6,12,15,22,23,24,25,26,27,28,29,30,31,40,41,42,43,58,63,80,90,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,116,119,122,123,127,128,129,131,132,],[17,17,-3,-5,-6,-7,17,-34,-35,-36,-33,-4,-8,-9,-10,-11,-12,17,-41,-42,-43,-44,-13,-37,-40,17,-67,17,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-38,-59,-14,-19,-39,17,17,-63,-15,-18,]),'PRINT':([0,2,3,4,5,6,12,15,22,23,24,25,26,27,28,29,30,31,40,41,42,43,58,63,80,90,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,116,119,122,123,127,128,129,131,132,],[19,19,-3,-5,-6,-7,19,-34,-35,-36,-33,-4,-8,-9,-10,-11,-12,19,-41,-42,-43,-44,-13,-37,-40,19,-67,19,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-38,-59,-14,-19,-39,19,19,-63,-15,-18,]),'BREAK':([0,2,3,4,5,6,12,15,22,23,24,25,26,27,28,29,30,31,40,41,42,43,58,63,80,90,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,116,119,122,123,127,128,129,131,132,],[20,20,-3,-5,-6,-7,20,-34,-35,-36,-33,-4,-8,-9,-10,-11,-12,20,-41,-42,-43,-44,-13,-37,-40,20,-67,20,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-38,-59,-14,-19,-39,20,20,-63,-15,-18,]),'CONTINUE':([0,2,3,4,5,6,12,15,22,23,24,25,26,27,28,29,30,31,40,41,42,43,58,63,80,90,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,116,119,122,123,127,128,129,131,132,],[21,21,-3,-5,-6,-7,21,-34,-35,-36,-33,-4,-8,-9,-10,-11,-12,21,-41,-42,-43,-44,-13,-37,-40,21,-67,21,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-38,-59,-14,-19,-39,21,21,-63,-15,-18,]),'ID':([0,2,3,4,5,6,12,14,15,17,19,22,23,24,25,26,27,28,29,30,31,32,35,37,39,40,41,42,43,48,49,50,51,52,58,60,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,79,80,81,89,90,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,116,119,120,122,123,125,127,128,129,131,132,],[24,24,-3,-5,-6,-7,24,24,-34,24,24,-35,-36,-33,-4,-8,-9,-10,-11,-12,24,24,24,24,24,-41,-42,-43,-44,24,24,24,24,24,-13,24,-37,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,-40,24,24,24,-67,24,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-38,-59,-14,24,-19,-39,24,24,24,-63,-15,-18,]),'}':([3,4,5,6,25,26,27,28,29,30,31,58,119,122,131,132,],[-3,-5,-6,-7,-4,-8,-9,-10,-11,-12,58,-13,-14,-19,-15,-18,]),'ELSE':([4,5,6,26,27,28,29,30,58,119,122,131,132,],[-5,-6,-7,-8,-9,-10,-11,-12,-13,127,-19,-15,-18,]),';':([7,8,9,10,11,15,17,20,21,22,23,24,36,40,41,42,43,53,54,55,56,57,63,80,84,85,86,87,88,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,116,118,123,129,],[26,27,28,29,30,-34,-16,-20,-21,-35,-36,-33,-17,-41,-42,-43,-44,-23,-24,-26,-27,-22,-37,-40,-28,-29,-30,-31,-32,-67,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-38,-59,-25,-39,-63,]),'(':([13,16,17,19,32,35,37,38,39,44,45,46,48,49,50,51,52,60,64,65,66,67,68,69,70,71,72,73,74,75,76,77,79,89,120,],[32,35,37,37,37,37,37,79,37,-60,-61,-62,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'=':([15,18,22,23,24,33,93,129,],[-34,48,-35,-36,-33,60,-67,-63,]),'ADDASSIGN':([15,18,22,23,24,93,129,],[-34,49,-35,-36,-33,-67,-63,]),'SUBASSIGN':([15,18,22,23,24,93,129,],[-34,50,-35,-36,-33,-67,-63,]),'MULASSIGN':([15,18,22,23,24,93,129,],[-34,51,-35,-36,-33,-67,-63,]),'DIVASSIGN':([15,18,22,23,24,93,129,],[-34,52,-35,-36,-33,-67,-63,]),"'":([15,22,23,24,36,40,41,42,43,55,59,62,63,78,80,84,85,86,87,88,91,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,123,128,129,],[-34,-35,-36,-33,63,-41,-42,-43,-44,63,63,63,-37,63,63,63,63,63,63,63,63,-67,63,63,63,63,63,63,63,63,63,63,63,63,63,63,-38,63,-59,-39,63,-63,]),'+':([15,22,23,24,36,40,41,42,43,55,59,62,63,78,80,84,85,86,87,88,91,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,123,128,129,],[-34,-35,-36,-33,64,-41,-42,-43,-44,64,64,64,-37,64,-40,64,64,64,64,64,64,-67,-45,-46,-47,-48,-49,-50,-51,-52,64,64,64,64,64,64,-38,64,-59,-39,64,-63,]),'-':([15,17,19,22,23,24,32,35,36,37,39,40,41,42,43,48,49,50,51,52,55,59,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,84,85,86,87,88,89,91,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,120,123,128,129,],[-34,39,39,-35,-36,-33,39,39,65,39,39,-41,-42,-43,-44,39,39,39,39,39,65,65,39,65,-37,39,39,39,39,39,39,39,39,39,39,39,39,39,39,65,39,-40,65,65,65,65,65,39,65,-67,-45,-46,-47,-48,-49,-50,-51,-52,65,65,65,65,65,65,-38,65,-59,39,-39,65,-63,]),'*':([15,22,23,24,36,40,41,42,43,55,59,62,63,78,80,84,85,86,87,88,91,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,123,128,129,],[-34,-35,-36,-33,66,-41,-42,-43,-44,66,66,66,-37,66,-40,66,66,66,66,66,66,-67,66,66,-47,-48,66,66,-51,-52,66,66,66,66,66,66,-38,66,-59,-39,66,-63,]),'/':([15,22,23,24,36,40,41,42,43,55,59,62,63,78,80,84,85,86,87,88,91,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,123,128,129,],[-34,-35,-36,-33,67,-41,-42,-43,-44,67,67,67,-37,67,-40,67,67,67,67,67,67,-67,67,67,-47,-48,67,67,-51,-52,67,67,67,67,67,67,-38,67,-59,-39,67,-63,]),'DOTADD':([15,22,23,24,36,40,41,42,43,55,59,62,63,78,80,84,85,86,87,88,91,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,123,128,129,],[-34,-35,-36,-33,68,-41,-42,-43,-44,68,68,68,-37,68,-40,68,68,68,68,68,68,-67,68,68,-47,-48,-49,-50,-51,-52,68,68,68,68,68,68,-38,68,-59,-39,68,-63,]),'DOTSUB':([15,22,23,24,36,40,41,42,43,55,59,62,63,78,80,84,85,86,87,88,91,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,123,128,129,],[-34,-35,-36,-33,69,-41,-42,-43,-44,69,69,69,-37,69,-40,69,69,69,69,69,69,-67,69,69,-47,-48,-49,-50,-51,-52,69,69,69,69,69,69,-38,69,-59,-39,69,-63,]),'DOTMUL':([15,22,23,24,36,40,41,42,43,55,59,62,63,78,80,84,85,86,87,88,91,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,123,128,129,],[-34,-35,-36,-33,70,-41,-42,-43,-44,70,70,70,-37,70,-40,70,70,70,70,70,70,-67,70,70,70,70,70,70,-51,-52,70,70,70,70,70,70,-38,70,-59,-39,70,-63,]),'DOTDIV':([15,22,23,24,36,40,41,42,43,55,59,62,63,78,80,84,85,86,87,88,91,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,123,128,129,],[-34,-35,-36,-33,71,-41,-42,-43,-44,71,71,71,-37,71,-40,71,71,71,71,71,71,-67,71,71,71,71,71,71,-51,-52,71,71,71,71,71,71,-38,71,-59,-39,71,-63,]),'>':([15,22,23,24,36,40,41,42,43,55,59,62,63,78,80,84,85,86,87,88,91,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,123,128,129,],[-34,-35,-36,-33,72,-41,-42,-43,-44,72,72,72,-37,72,-40,72,72,72,72,72,72,-67,-45,-46,-47,-48,-49,-50,-51,-52,None,None,None,None,None,None,-38,72,-59,-39,72,-63,]),'<':([15,22,23,24,36,40,41,42,43,55,59,62,63,78,80,84,85,86,87,88,91,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,123,128,129,],[-34,-35,-36,-33,73,-41,-42,-43,-44,73,73,73,-37,73,-40,73,73,73,73,73,73,-67,-45,-46,-47,-48,-49,-50,-51,-52,None,None,None,None,None,None,-38,73,-59,-39,73,-63,]),'EQ':([15,22,23,24,36,40,41,42,43,55,59,62,63,78,80,84,85,86,87,88,91,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,123,128,129,],[-34,-35,-36,-33,74,-41,-42,-43,-44,74,74,74,-37,74,-40,74,74,74,74,74,74,-67,-45,-46,-47,-48,-49,-50,-51,-52,None,None,None,None,None,None,-38,74,-59,-39,74,-63,]),'NEQ':([15,22,23,24,36,40,41,42,43,55,59,62,63,78,80,84,85,86,87,88,91,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,123,128,129,],[-34,-35,-36,-33,75,-41,-42,-43,-44,75,75,75,-37,75,-40,75,75,75,75,75,75,-67,-45,-46,-47,-48,-49,-50,-51,-52,None,None,None,None,None,None,-38,75,-59,-39,75,-63,]),'LEQ':([15,22,23,24,36,40,41,42,43,55,59,62,63,78,80,84,85,86,87,88,91,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,123,128,129,],[-34,-35,-36,-33,76,-41,-42,-43,-44,76,76,76,-37,76,-40,76,76,76,76,76,76,-67,-45,-46,-47,-48,-49,-50,-51,-52,None,None,None,None,None,None,-38,76,-59,-39,76,-63,]),'GEQ':([15,22,23,24,36,40,41,42,43,55,59,62,63,78,80,84,85,86,87,88,91,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,123,128,129,],[-34,-35,-36,-33,77,-41,-42,-43,-44,77,77,77,-37,77,-40,77,77,77,77,77,77,-67,-45,-46,-47,-48,-49,-50,-51,-52,None,None,None,None,None,None,-38,77,-59,-39,77,-63,]),',':([15,22,23,24,40,41,42,43,53,54,55,56,57,61,63,80,82,83,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,111,112,113,114,115,116,118,123,124,126,129,130,],[-34,-35,-36,-33,-41,-42,-43,-44,89,-24,-26,-27,-22,92,-37,-40,117,-65,-67,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-38,125,-69,-70,-71,-72,-59,-25,-39,-66,-64,-63,-68,]),')':([15,22,23,24,40,41,42,43,59,62,63,78,80,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,116,123,129,],[-34,-35,-36,-33,-41,-42,-43,-44,90,94,-37,109,-40,-67,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-38,123,-59,-39,-63,]),':':([15,22,23,24,40,41,42,43,63,80,91,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,116,123,129,],[-34,-35,-36,-33,-41,-42,-43,-44,-37,-40,120,-67,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-38,-59,-39,-63,]),']':([15,22,23,24,61,82,83,93,111,112,113,114,115,121,124,126,129,130,],[-34,-35,-36,-33,93,116,-65,-67,124,-69,-70,-71,-72,129,-66,-64,-63,-68,]),'[':([15,17,19,24,32,35,37,39,47,48,49,50,51,52,60,64,65,66,67,68,69,70,71,72,73,74,75,76,77,79,89,117,120,],[34,47,47,-33,47,47,47,47,81,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,81,47,]),'INTNUM':([17,19,32,34,35,37,39,48,49,50,51,52,60,64,65,66,67,68,69,70,71,72,73,74,75,76,77,79,81,89,92,120,125,],[42,42,42,61,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,113,42,121,42,113,]),'FLOAT':([17,19,32,35,37,39,48,49,50,51,52,60,64,65,66,67,68,69,70,71,72,73,74,75,76,77,79,81,89,120,125,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,114,43,43,114,]),'ZEROS':([17,19,32,35,37,39,48,49,50,51,52,60,64,65,66,67,68,69,70,71,72,73,74,75,76,77,79,89,120,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'ONES':([17,19,32,35,37,39,48,49,50,51,52,60,64,65,66,67,68,69,70,71,72,73,74,75,76,77,79,89,120,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'EYE':([17,19,32,35,37,39,48,49,50,51,52,60,64,65,66,67,68,69,70,71,72,73,74,75,76,77,79,89,120,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'STRING':([19,89,],[57,57,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'instructions':([0,12,],[2,31,]),'instr':([0,2,12,31,90,94,127,128,],[3,25,3,25,119,122,131,132,]),'instr_if':([0,2,12,31,90,94,127,128,],[4,4,4,4,4,4,4,4,]),'instr_for':([0,2,12,31,90,94,127,128,],[5,5,5,5,5,5,5,5,]),'instr_while':([0,2,12,31,90,94,127,128,],[6,6,6,6,6,6,6,6,]),'instr_return':([0,2,12,31,90,94,127,128,],[7,7,7,7,7,7,7,7,]),'instr_assign':([0,2,12,31,90,94,127,128,],[8,8,8,8,8,8,8,8,]),'instr_print':([0,2,12,31,90,94,127,128,],[9,9,9,9,9,9,9,9,]),'break':([0,2,12,31,90,94,127,128,],[10,10,10,10,10,10,10,10,]),'continue':([0,2,12,31,90,94,127,128,],[11,11,11,11,11,11,11,11,]),'id':([0,2,12,14,17,19,31,32,35,37,39,48,49,50,51,52,60,64,65,66,67,68,69,70,71,72,73,74,75,76,77,79,81,89,90,94,120,125,127,128,],[15,15,15,33,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'assignable':([0,2,12,17,19,31,32,35,37,39,48,49,50,51,52,60,64,65,66,67,68,69,70,71,72,73,74,75,76,77,79,81,89,90,94,120,125,127,128,],[18,18,18,40,40,18,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,115,40,18,18,40,115,18,18,]),'matrix_element':([0,2,12,17,19,31,32,35,37,39,48,49,50,51,52,60,64,65,66,67,68,69,70,71,72,73,74,75,76,77,79,81,89,90,94,120,125,127,128,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'vector_element':([0,2,12,17,19,31,32,35,37,39,48,49,50,51,52,60,64,65,66,67,68,69,70,71,72,73,74,75,76,77,79,81,89,90,94,120,125,127,128,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'expr':([17,19,32,35,37,39,48,49,50,51,52,60,64,65,66,67,68,69,70,71,72,73,74,75,76,77,79,89,120,],[36,55,59,62,78,80,84,85,86,87,88,91,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,55,128,]),'matrix_create':([17,19,32,35,37,39,48,49,50,51,52,60,64,65,66,67,68,69,70,71,72,73,74,75,76,77,79,89,120,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'matrix':([17,19,32,35,37,39,48,49,50,51,52,60,64,65,66,67,68,69,70,71,72,73,74,75,76,77,79,89,120,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'printables':([19,],[53,]),'printable':([19,89,],[54,118,]),'str':([19,89,],[56,56,]),'vectors':([47,],[82,]),'vector':([47,117,],[83,126,]),'variables':([81,],[111,]),'variable':([81,125,],[112,130,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> <empty>','start',0,'p_start','Mparser.py',32),
  ('start -> instructions','start',1,'p_start','Mparser.py',33),
  ('instructions -> instr','instructions',1,'p_instructions','Mparser.py',37),
  ('instructions -> instructions instr','instructions',2,'p_instructions','Mparser.py',38),
  ('instr -> instr_if','instr',1,'p_instr','Mparser.py',42),
  ('instr -> instr_for','instr',1,'p_instr','Mparser.py',43),
  ('instr -> instr_while','instr',1,'p_instr','Mparser.py',44),
  ('instr -> instr_return ;','instr',2,'p_instr','Mparser.py',45),
  ('instr -> instr_assign ;','instr',2,'p_instr','Mparser.py',46),
  ('instr -> instr_print ;','instr',2,'p_instr','Mparser.py',47),
  ('instr -> break ;','instr',2,'p_instr','Mparser.py',48),
  ('instr -> continue ;','instr',2,'p_instr','Mparser.py',49),
  ('instr -> { instructions }','instr',3,'p_scope','Mparser.py',54),
  ('instr_if -> IF ( expr ) instr','instr_if',5,'p_instr_if','Mparser.py',59),
  ('instr_if -> IF ( expr ) instr ELSE instr','instr_if',7,'p_instr_if','Mparser.py',60),
  ('instr_return -> RETURN','instr_return',1,'p_instr_return','Mparser.py',65),
  ('instr_return -> RETURN expr','instr_return',2,'p_instr_return','Mparser.py',66),
  ('instr_for -> FOR id = expr : expr instr','instr_for',7,'p_instr_for','Mparser.py',72),
  ('instr_while -> WHILE ( expr ) instr','instr_while',5,'p_instr_while','Mparser.py',77),
  ('break -> BREAK','break',1,'p_break','Mparser.py',82),
  ('continue -> CONTINUE','continue',1,'p_continue','Mparser.py',87),
  ('str -> STRING','str',1,'p_str','Mparser.py',93),
  ('instr_print -> PRINT printables','instr_print',2,'p_instr_print','Mparser.py',98),
  ('printables -> printable','printables',1,'p_printables','Mparser.py',103),
  ('printables -> printables , printable','printables',3,'p_printables','Mparser.py',104),
  ('printable -> expr','printable',1,'p_printable','Mparser.py',109),
  ('printable -> str','printable',1,'p_printable','Mparser.py',110),
  ('instr_assign -> assignable = expr','instr_assign',3,'p_instr_assign','Mparser.py',116),
  ('instr_assign -> assignable ADDASSIGN expr','instr_assign',3,'p_instr_assign','Mparser.py',117),
  ('instr_assign -> assignable SUBASSIGN expr','instr_assign',3,'p_instr_assign','Mparser.py',118),
  ('instr_assign -> assignable MULASSIGN expr','instr_assign',3,'p_instr_assign','Mparser.py',119),
  ('instr_assign -> assignable DIVASSIGN expr','instr_assign',3,'p_instr_assign','Mparser.py',120),
  ('id -> ID','id',1,'p_id','Mparser.py',124),
  ('assignable -> id','assignable',1,'p_assignable','Mparser.py',128),
  ('assignable -> matrix_element','assignable',1,'p_assignable','Mparser.py',129),
  ('assignable -> vector_element','assignable',1,'p_assignable','Mparser.py',130),
  ("expr -> expr '",'expr',2,'p_expr_trans','Mparser.py',136),
  ('expr -> ( expr )','expr',3,'p_expr_nested','Mparser.py',140),
  ('expr -> matrix_create ( expr )','expr',4,'p_expr_matrix_create','Mparser.py',144),
  ('expr -> - expr','expr',2,'p_expr_minus','Mparser.py',148),
  ('expr -> assignable','expr',1,'p_expr_literal','Mparser.py',152),
  ('expr -> matrix','expr',1,'p_expr_literal','Mparser.py',153),
  ('expr -> INTNUM','expr',1,'p_expr_int','Mparser.py',157),
  ('expr -> FLOAT','expr',1,'p_expr_float','Mparser.py',161),
  ('expr -> expr + expr','expr',3,'p_binary_expr','Mparser.py',165),
  ('expr -> expr - expr','expr',3,'p_binary_expr','Mparser.py',166),
  ('expr -> expr * expr','expr',3,'p_binary_expr','Mparser.py',167),
  ('expr -> expr / expr','expr',3,'p_binary_expr','Mparser.py',168),
  ('expr -> expr DOTADD expr','expr',3,'p_binary_expr','Mparser.py',169),
  ('expr -> expr DOTSUB expr','expr',3,'p_binary_expr','Mparser.py',170),
  ('expr -> expr DOTMUL expr','expr',3,'p_binary_expr','Mparser.py',171),
  ('expr -> expr DOTDIV expr','expr',3,'p_binary_expr','Mparser.py',172),
  ('expr -> expr > expr','expr',3,'p_binary_expr','Mparser.py',173),
  ('expr -> expr < expr','expr',3,'p_binary_expr','Mparser.py',174),
  ('expr -> expr EQ expr','expr',3,'p_binary_expr','Mparser.py',175),
  ('expr -> expr NEQ expr','expr',3,'p_binary_expr','Mparser.py',176),
  ('expr -> expr LEQ expr','expr',3,'p_binary_expr','Mparser.py',177),
  ('expr -> expr GEQ expr','expr',3,'p_binary_expr','Mparser.py',178),
  ('matrix -> [ vectors ]','matrix',3,'p_matrix','Mparser.py',185),
  ('matrix_create -> ZEROS','matrix_create',1,'p_matrix_create','Mparser.py',189),
  ('matrix_create -> ONES','matrix_create',1,'p_matrix_create','Mparser.py',190),
  ('matrix_create -> EYE','matrix_create',1,'p_matrix_create','Mparser.py',191),
  ('matrix_element -> id [ INTNUM , INTNUM ]','matrix_element',6,'p_matrix_element','Mparser.py',196),
  ('vectors -> vectors , vector','vectors',3,'p_vectors','Mparser.py',202),
  ('vectors -> vector','vectors',1,'p_vectors','Mparser.py',203),
  ('vector -> [ variables ]','vector',3,'p_vector','Mparser.py',207),
  ('vector_element -> id [ INTNUM ]','vector_element',4,'p_vector_element','Mparser.py',211),
  ('variables -> variables , variable','variables',3,'p_variables','Mparser.py',217),
  ('variables -> variable','variables',1,'p_variables','Mparser.py',218),
  ('variable -> INTNUM','variable',1,'p_variable','Mparser.py',223),
  ('variable -> FLOAT','variable',1,'p_variable','Mparser.py',224),
  ('variable -> assignable','variable',1,'p_variable','Mparser.py',225),
]
