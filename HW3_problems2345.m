%% 2E

P = [.9 .1 0 ; 0 7/8 1/8; .4 0 .6];

P ^ 50

%% 2F
clc
n = 0;
A = 10000;
state = 1;
for j = 1:A
    cumulative = 0;
    U = rand();
        
    k = 0;
    while(cumulative < U)
        k = k+1;
        cumulative = cumulative + P(state, k);

    end
    state = k;
    n = n + (state == 1);
end


n / A

%% 3
P = [1 0 0 0 0; 1/3 0 2/3 0 0; 0 1/3 0 2/3 0; 0 0 1/3 0 2/3; 0 0 0 0 1];
P^5

%% 4

P = [.5 .5 0 0 0 0; 0 .5 .5 0 0 0; 1/3 0 1/3 1/3 0 0;0 0 0 .5 .5 0; 0 0 0 0 0 1; 0 0 0 0 1 0];

P ^ 5 


%% 4C
clc
n = 0;
A = 10000;
for i = 1:A
    state = 1;
    for j = 1:5
        cumulative = 0;
        U = rand();
            
        k = 0;
        while(cumulative < U)
            k = k+1;
            cumulative = cumulative + P(state, k);

        end
        state = k;
    end
    n = n + (state == 4);
end

n / A