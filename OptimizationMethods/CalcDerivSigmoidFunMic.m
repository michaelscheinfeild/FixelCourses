function [fx] = CalcDerivSigmoidFunMic(Vx)

sigm = 1./(1+exp(-Vx));

fx = 2*sigm*(1-sigm);