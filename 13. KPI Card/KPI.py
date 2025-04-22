import matplotlib.pyplot as plt,pandas as pd,numpy as np
D= https://raw.githubusercontent.com/rayansaud01/Excel/main/13. KPIs v2.xlsx
D['M']=D.Month.map({'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12})
d=D.groupby(['Year','M']).Sales.sum().unstack(fill_value=0)
Y=list(d.index);ly,py=Y[-1],Y[-2]
L,P=d.loc[ly],d.loc[py]
a,b=L.sum(),P.sum();c=(a-b)/b*100 if b else 0;u,cl=('▲','green')if c>=0 else('▼','red');pt=f"{u}{abs(c):.1f}% vs {py}"
m=list(range(1,13));lbl=list("JFMAMJJASOND")
mn=pd.concat([L,P]).dropna();lo,hi=mn.min()*.9,mn.max()*1.2
fmt=lambda x:('N/A'if np.isnan(x)else next((f"${x/v:,.0f}{s}"for v,s in((1e9,'B'),(1e6,'M'),(1e3,'K'))if x>=v),f"${x:,.0f}"))
fig,ax=plt.subplots(3,5,figsize=(24,10),facecolor='w',gridspec_kw={'hspace':.8,'wspace':.3});axs=ax.flatten()
# legend
axs[0].axis('off')
axs[0].text(.1,1,"Excel KPI Cards",fontsize=20,weight='bold',color='gray')
axs[0].text(.1,.5,"LY > PY",fontsize=16,weight='bold',color='green')
axs[0].text(.4,.5,"|",fontsize=16,weight='bold',color='gray')
axs[0].text(.45,.5,"LY < PY",fontsize=16,weight='bold',color='red')
axs[0].text(.1,.2,"■ Latest Year",fontsize=16,weight='bold',color='#003049')
axs[0].text(.1,.05,"■ Previous Year",fontsize=16,weight='bold',color='lightgray')
# centered header
axs[1].axis('off')
axs[1].text(.5,.8,str(ly),transform=axs[1].transAxes,fontsize=14,ha='center')
axs[1].text(.5,.6,fmt(a),transform=axs[1].transAxes,fontsize=24,weight='bold',color='#03045e',ha='center')
axs[1].text(.5,.4,pt,transform=axs[1].transAxes,fontsize=12,color=cl,ha='center')
# row1 charts
for i in [2,3,4]:
    ax=axs[i]
    ax.text(.05,1.35,str(ly),transform=ax.transAxes,fontsize=14)
    ax.text(.05,1.16,fmt(a),transform=ax.transAxes,fontsize=24,weight='bold',color='#03045e')
    ax.text(.05,1.05,pt,transform=ax.transAxes,fontsize=12,color=cl)
    if i<4:
        ax.spines.values().__iter__().__next__()  # ensure spines visible
        ax.axis('on')
        ax.set_xlabel('Month',fontsize=9,color='gray'); ax.set_ylabel('Sales',fontsize=9,color='gray')
        ax.set_xticks(m); ax.set_xticklabels(lbl,fontsize=9,color='gray')
        yt=np.linspace(lo,hi,4)
        ax.set_yticks(yt); ax.set_yticklabels([fmt(v) for v in yt],fontsize=9,color='gray')
        ax.set_xlim(.5,12.5); ax.set_ylim(lo,hi)
        if i==2: ax.step(m,L,where='mid',color='#003049',linewidth=2)
        if i==3: ax.step(m,P,where='mid',color='lightgray',linewidth=2); ax.step(m,L,where='mid',color='#003049',linewidth=2)
    else:
        ax.axis('off')
        mx=max(a,b)*1.2; ax.set_xlim(0,mx); ax.set_ylim(-.5,.5)
        ax.barh(0,a,height=.2,color='#003049'); ax.plot([b]*2,[-.2,.2],color='lightgray',linewidth=2)
        ax.text(a,0.2,f"{a/1e6:.0f}M",va='bottom',ha='left',fontsize=9,color='#003049')
        ax.text(b,-0.2,f"{b/1e6:.0f}M",va='top',ha='right',fontsize=9,color='gray')
# row2 charts
for i in range(5,10):
    ax=axs[i]; ax.axis('on')
    ax.set_xlabel('Month',fontsize=9,color='gray'); ax.set_ylabel('Sales',fontsize=9,color='gray')
    ax.set_xticks(m); ax.set_xticklabels(lbl,fontsize=9,color='gray')
    yt=np.linspace(lo,hi,4)
    ax.set_yticks(yt); ax.set_yticklabels([fmt(v) for v in yt],fontsize=9,color='gray')
    ax.set_xlim(.5,12.5); ax.set_ylim(lo,hi)
    ax.text(.05,1.35,str(ly),transform=ax.transAxes,fontsize=14)
    ax.text(.05,1.16,fmt(a),transform=ax.transAxes,fontsize=24,weight='bold',color='#03045e')
    ax.text(.05,1.05,pt,transform=ax.transAxes,fontsize=12,color=cl)
    if i==5: ax.bar(m,P,color='lightgray',width=.8); ax.step(m,L,where='mid',color='#003049',linewidth=2)
    if i==6: ax.bar(m,L,color=['#2a9d8f'if L[j]>=P[j]else'#FC5D65'for j in m],width=.8)
    if i==7: ax.bar(m,P,color='lightgray',width=.8); ax.bar(m,L,color='#003049',width=.5)
    if i==8: ax.bar(m,P,color='lightgray',width=.8); ax.bar(m,L,color=['#2a9d8f'if L[j]>=P[j]else'#FC5D65'for j in m],width=.5)
    if i==9: ax.bar(m,L,color=['#2a9d8f'if L[j]>=P[j]else'#FC5D65'for j in m],width=.8); [ax.hlines(P[j],j-.4,j+.4,color='lightgray',linewidth=2) for j in m]
# row3 panels
# pct change
ax = axs[10]; ax.axis('on')
ax.spines['left'].set_visible(True)
ax.set_xlabel('Month', fontsize=9, color='gray'); ax.set_ylabel('% Change', fontsize=9, color='gray')
ax.set_xticks(m); ax.set_xticklabels(lbl, fontsize=9, color='gray')
# Calculate percentage changes
pc = [((L[j] - P[j]) / P[j] * 100) if P[j] != 0 else np.nan for j in m]
# Set y-axis limits based on pc
pc_valid = [p for p in pc if not np.isnan(p)]
if pc_valid:
    lo_pc = min(pc_valid) - 0.1 * (max(pc_valid) - min(pc_valid) or 1)
    hi_pc = max(pc_valid) + 0.1 * (max(pc_valid) - min(pc_valid) or 1)
else:
    lo_pc, hi_pc = -100, 100
yt = np.linspace(lo_pc, hi_pc, 4)
ax.set_yticks(yt); ax.set_yticklabels([f"{v:.0f}%" for v in yt], fontsize=9, color='gray')
ax.set_ylim(lo_pc, hi_pc)
ax.bar(m, pc, color=[('#2a9d8f' if p >= 0 else '#FC5D65') for p in pc], width=.8)
# Add text
ax.text(.05, 1.35, str(ly), transform=ax.transAxes, fontsize=14)
ax.text(.05, 1.16, fmt(a), transform=ax.transAxes, fontsize=24, weight='bold', color='#03045e')
ax.text(.05, 1.05, pt, transform=ax.transAxes, fontsize=12, color=cl)
# comparison
for k,i in enumerate(range(11,15),1):
    ax=axs[i]; ax.axis('on')
    ax.text(.05,1.35,str(ly),transform=ax.transAxes,fontsize=14)
    ax.text(.05,1.16,fmt(a),transform=ax.transAxes,fontsize=24,weight='bold',color='#03045e')
    ax.text(.05,1.05,pt,transform=ax.transAxes,fontsize=12,color=cl)
    if k<=2:
        # x sales, y month
        xt=np.linspace(lo,hi,4)
        ax.set_xticks(xt); ax.set_xticklabels([fmt(v) for v in xt],fontsize=9,color='gray')
        ax.set_yticks(m); ax.set_yticklabels(lbl,fontsize=9,color='gray')
        ax.set_xlabel('Sales',fontsize=9,color='gray'); ax.set_ylabel('Month',fontsize=9,color='gray')
    else:
        # x month, y sales
        ax.set_xticks(m); ax.set_xticklabels(lbl,fontsize=9,color='gray')
        yt=np.linspace(lo,hi,4)
        ax.set_yticks(yt); ax.set_yticklabels([fmt(v) for v in yt],fontsize=9,color='gray')
        ax.set_xlabel('Month',fontsize=9,color='gray'); ax.set_ylabel('Sales',fontsize=9,color='gray')
    for j in m:
        co='#2a9d8f' if L[j]>=P[j] else '#FC5D65'
        if k==1: ax.plot([P[j],L[j]],[j,j],color=co,linewidth=2,solid_capstyle='round'); ax.plot(L[j],j,'o',markersize=8,color=co)
        if k==2: ax.plot([P[j],L[j]],[j,j],linewidth=9,color=co); ax.plot(P[j],j,'o',markersize=8,color='lightgray'); ax.plot(L[j],j,'o',markersize=8,color='#003049')
        if k==3:
                height = abs(L[j] - P[j])
                bottom = min(L[j], P[j])
                rect = plt.matplotlib.patches.FancyBboxPatch(
                    (j - 0.3, bottom),  
                    0.6,                
                    height,             
                    boxstyle="round,pad=0.02,rounding_size=3",
                    linewidth=0,
                    facecolor=co,
                    edgecolor=co,
                    mutation_aspect=0.5
                )
                ax.add_patch(rect)

        if k==4: ax.plot([j,j],[P[j],L[j]]); ax.plot(j,P[j],'o',markersize=8,color='lightgray'); ax.plot(j,L[j],'o',markersize=8,color='#003049')
plt.show()

