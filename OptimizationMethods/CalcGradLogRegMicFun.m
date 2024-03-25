function [vX] = CalcGradLogRegMicFun(vX, mX, vY)

sig = CalcSigmoidFun(vX*mX);


vX = sig*(1-sig)*(sig-vY);
end