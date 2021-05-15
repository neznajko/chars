# Character Recognition

***[Ok]***, no need for Neural Networks here, 
[clck!](https://ioinformatics.org/files/ioi1997problem5.pdf)
**The** program is super simple, I've made template letters only
for first *8* characters cos I've got lazy:), not good. ***The***
images are represented as sequences of *0s* and *1s* so we don't
need fancy math here either. *For* classifying the characters the
program is computing the *distance* between corresponding arrays,
by using some cool features of the ***numpy*** module. **Here** is
an output for the corrupted image of **e** az an example:

```Python
%%%%%%%%% %%
%%%%%%%%% %%
%%%%%%%%   %
 %%% %% %%%%
% %%% %%%%%
%%  %%% %%%%
 %%%%    %%%
%%  %%%% %%
%%   %%%  %%
%%    %   %%
%%  %%%%  %%
%% % %% %% %
%%%       %%
 %%%% %%%%%%
% % %%%%%%%%

e
```

[Master Of Puppets](https://youtu.be/0p9CB5imSes)
