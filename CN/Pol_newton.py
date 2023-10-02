def interp_newton_coeffs(xvals,yvals):
    nbr_data_points = len(xvals)
    depth =1
    coeffs = [yvals[0]]
    iter_yvals = yvals
    while depth < nbr_data_points:
        iterdata=[]
        for i in range(len(iter_yvals)-1):
            delta_y= iter_yvals[i+1]-iter_yvals[i]
            delta_x= xvals[i+depth]-xvals[i]
            interval = (delta_y/delta_x)
            iterdata.append(interval)
            if i==0: coeffs.append(interval)
        iter_yvals=iterdata
        depth+=1
    return coeffs

def newton_pol(xvals,coeffs):
    def f(i):
        terms = []
        retval = 0
        for j in range(len(coeffs)):
            iterval = coeffs[j]
            iterxvals = xvals[:j]
            for k in iterxvals: iterval*=(i-k)
            terms.append(iterval)
            retval+=iterval
        return(retval)
    return(f)

xvals=[0,1,2,4,5]
yvals=[2,3,10,66,127]

coeffs = interp_newton_coeffs(xvals, yvals)
pol=newton_pol(xvals,coeffs)
print(pol(2.5))