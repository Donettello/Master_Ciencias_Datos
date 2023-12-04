#####################################################
#
#  Project: Demos for stochastic processes 2023-24
#  File:    gwalk.py
#  Rev.     1.0
#  Date:    11/10/2023
#
#  Simulation of one (or a number of) random walks in a graph
#
#
import random



#####################################################
#
# Returns the m nodes to which a new node will connect, chosen using
# the "rich gets richer" tstrategy
#
def conn_sel(G, m):
    res = []
    candidates = list(range(len(G)))
    for k in range(m):
        norm = sum([len(G[k]) for k in candidates])
        r = random.randint(0,norm)
        s = 0
        for k in range(len(candidates)):
            s += len(G[candidates[k]])
            if s >= r:
                res += [candidates[k]]
                candidates = candidates[:k] + candidates[k+1:]
                break
    return res


#####################################################
#
# Creates a Barabasi graph. A graph is simply a list of lists, the
# node id is the index in the list and the associated list is the
# adjacency list of the node
#
#
def barabasi(N, m):
    #
    # Make a fully connected graph with m nodes
    G = [ [n for n in range(m) if n != k] for k in range(m)]

    #
    # Now start adding nodes
    #
    for k in range(N-m):
        adj = conn_sel(G, m)
        G += [adj]    # add the new node
        id = len(G)-1
        for k in adj:   # The graph is undirected: add a link to the new node to all its connections
            G[k] += [id]
    return G


#
# Given a graph and the node in which the walker is positiones,
# returns the new node of the walk chosen randomly among the neighbors
# of the node
#
def step(G, k):
    u = len(G[k])
    return G[k][random.randint(0,u-1)]


#
# Given a list of graph and a list indicating in which node the walk
# is positioned in each one of the graphs, returns a list with the new
# position after a random step to one of the neighbors
#
def multistep(Glst, pos):
    newpos = []
    for (g, n) in zip(Glst, pos):
        newpos += [step(g, n)]
    return newpos

#
# Given a list of nodes on which the walk is (or has been) positioned
# (and the maximum node number), returns a vector with the fraction of
# times that the walk has been on each one of the nodes. That is,
# returns an estimation of the occupancy probability
#
def pcalc(pos, nmax):
    freq = nmax*[0.0]
    for k in pos:
        freq[k] += 1.0
    w = float(sum(freq))
    return [float(x)/w for x in freq]

N = 100
m = 4
G = barabasi(N, m)



n = 5
pos = []
for k in range(2000):
    n = step(G, n)
    pos += [n]

res = []
for (g, p) in zip(G, pcalc(pos, N)):
    res += [(len(g), p)]

res = sorted(res, key=lambda x : x[0])

for (l, p) in res:
    print (l, p)
