# -*- coding: utf-8 -*-
"""
Created on Mon May 14 16:02:12 2018

@author: Binish125
"""

import random

pop_size=400
Num_items=15
Num_items=Num_items-1
tot_capacity=10
sim_run=4
val=[1,4,5,7,10,5,9,4,8,11,5,10,12,4,9]
wt=[1,3,4,5,4,2,3,6,8,4,1,2,6,5,1]
generations=50



def weighted_choice(items):
    weight_total=sum((item[1] for item in items))
    n=random.uniform(0,weight_total)
    for item,weight in items:
        if n<weight:
            return item;
        n=n-weight
    return item
        

def random_num():
    return(random.randint(0,Num_items))


def random_pop():
    pop=[]
    for i in range(pop_size):
        items=[]
        for j in range(Num_items):
            random_item=random_num()
            if(random_item not in items):
                items.append(random_item)
        pop.append(items)
    return(pop)


def fitness(dna,wt,val):
    fit=0
    weight=0
    for item in dna:
        weight+=wt[item]
        fit+=val[item]
    if(weight>tot_capacity):
        return(0) 
    return(fit)

def mutation(dna,wt,val):
    dna_out=[]
    mutation_chance=200
    for c in dna:
        mutation=int(mutation_chance*random.random())
        if(mutation>1 and mutation<5):
            rand_no=random_num()
            if(rand_no not in dna_out):
                dna_out.append(rand_no)
        else:
            if(c not in dna_out):
                dna_out.append(c)
    return(dna_out)        

def crossover(dna1,dna2):
    pos=int(random.random()*(Num_items))
    return(dna1[:pos]+list(set(dna2[pos:])-set(dna1[:pos])),dna2[:pos]+list(set(dna1[pos:])-set(dna2[:pos])))
       
if __name__== "__main__":
    output=[]
    for run in range(sim_run):
        print("\n\n\tSimulation Run "+ str(run+1)+" :\n")
        population=random_pop()          
        for generation in range(generations):
            fittest_population=population[0]
            maximum_fitness=fitness(population[0],wt,val)
            for individual in population:
                indi_fitness=fitness(individual,wt,val)
                if(indi_fitness>=maximum_fitness):
                    maximum_fitness=indi_fitness
                    fittest_population=individual
                
            print("Generation : "+ str(generation) + " random sample : "+ str(population[0]) + " - fittest population: "+ str(fittest_population)+ "  fitness : "+ str(maximum_fitness))
            
            weighted_pop=[]
            for individual in population:
                fitness_val=fitness(individual,wt,val)
                if(fitness_val==0):
                    pair=(individual,1.0)
                else:
                    pair=(individual,fitness_val*1.0)
                weighted_pop.append(pair)
            
            population=[]
            index=random.randint(0,pop_size/2)
            for i in range(int(pop_size/2)):
                ind1=weighted_choice(weighted_pop)
                ind2=weighted_choice(weighted_pop)
                ind1,ind2=crossover(ind1,ind2)
                inter=ind1+list(set(ind2)-set(ind1))
                if(i==index):
                    population.append(fittest_population)
                else:
                    population.append(mutation(ind1,wt,val))
                population.append(mutation(ind2,wt,val))
        output_pair=(fittest_population,maximum_fitness)
        output.append(output_pair)
        
    print("\n")
    best_pop=output[0][0]
    max_value=output[0][1]
    for out_pop, max_fit in output:
        print("Fittest Population: "+ str(out_pop)+ "  Fitness : "+ str(max_fit))
        if(max_value<=max_fit):
            max_value=max_fit
            best_pop=out_pop
            
    print("\n\nBest Population: \t"+str(best_pop))
    print("Maximum Fitness: \t"+str(max_value))