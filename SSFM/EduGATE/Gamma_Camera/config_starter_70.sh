#!/bin/csh
# file config_starter70.sh

source /Applications/gate_v7.0-install/env_gate.csh
root -l 'GenerateGateConfiguration.C( "Gamma_Camera.txt" )'
Gate Gamma_Camera.mac
root -l Gamma_Camera.C
