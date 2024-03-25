function [f] = CalcFrobNormObjFunMic(mx,my)

f = 0.5*norm(mx-my);