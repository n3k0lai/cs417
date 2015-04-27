

function f(x)
   return cos(x) - x*x*x;
end

[[--s,t: endpoints of an interval where we search
   e: half of upper bound for relative error
   m: maximal number of iterations --]]
function FalsiMethod(double s, double t, double e, int m)
    double r,fr;
    int n, side=0;
    -- starting values at endpoints of interval
    double fs = f(s);
    double ft = f(t);

    for n = 0, m do
        r = (fs*t - ft*s) / (fs - ft);
        if (fabs(t-s) < e*fabs(t+s)) break;
        fr = f(r);

        if (fr * ft > 0)
            -- fr and ft have same sign, copy r to t
            t, ft = r, fr
            if (side==-1)
                fs /= 2;
            end
            side = -1;
        else if (fs * fr > 0)
            -- fr and fs have same sign, copy r to s */
            s = r;  fs = fr;
            if (side==+1) ft /= 2;
            side = +1;
        else
            -- fr * f_ very small (looks like zero) */
            break;
        end
    end
    return r;
end