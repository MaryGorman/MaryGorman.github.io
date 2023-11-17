https://joey711.github.io/phyloseq/plot_tree-examples.html
https://matthewsmith.rbind.io/post/network-visualisation-in-r-package-comparison/
https://plotly.com/ggplot2/network-graphs/
https://briatte.github.io/ggnet/
https://yunranchen.github.io/intro-net-r/advanced-network-visualization.html
https://rpubs.com/geock/nv
https://nrennie.rbind.io/blog/2022-06-06-creating-flowcharts-with-ggplot2/


https://www.r-bloggers.com/2020/04/visualizing-multilevel-networks-with-graphlayouts/

https://masalmon.eu/2018/06/18/mathtree/

https://ggplot2-book.org/networks.html

https://www.r-bloggers.com/2019/06/interactive-network-visualization-with-r/

http://www.sthda.com/english/articles/33-social-network-analysis/135-network-visualization-essentials-in-r/

https://www.bioconductor.org/packages/devel/bioc/vignettes/RedeR/inst/doc/RedeR.html

http://brucedesmarais.com/Tutorial.html


# https://yunranchen.github.io/intro-net-r/igraph.html




```{r}
# http://blog.schochastics.net/post/visualizing-multilevel-networks-with-graphlayouts/
# library(graphlayouts)
# library(igraph)
# library(graphlayouts) 
# library(ggraph)
# library(threejs)
# 
# main$lvl <- main$Generation
# g <- igraph::graph_from_data_frame(main,directed=TRUE)
# 
# xy <- layout_as_multilevel(g,type = "separate", alpha = 25, beta = 45)
# 
# plot.igraph(g,vertex.label.dist=5.5,
#             vertex.color=as.factor(V(g)$lvl))
```


```{r}
# library(ggnetwork)
# library("GGally")
# library("geomnet")
# library("statnet")
# library(tidyverse)
# 
# data("football",package = "geomnet")
# rownames(football$vertices) <-football$vertices$label
# fb.net=network::network(football$edges[,1:2])
# 
# # add vertex attribute: the conference the team is in
# fb.net %v% "conf" <-football$vertices[network.vertex.names(fb.net), "value"]
# # add edge attribute: whether two teams belong to the same conference
# set.edge.attribute(fb.net, "same.conf",football$edges$same.conf)
# set.edge.attribute(fb.net, "lty", ifelse(fb.net %e% "same.conf" == 1, 1, 2))
# 
# main <- main %>% replace_na(replace=list(Female_Name="blank",Male_Name="blank"))
# 
# net <- network::network(main,multiple = TRUE)
# 
# ggnet2(net)
```

```{r}

# devtools::install_github("briatte/ggnet")
# library(plotly)
# library(ggnet)
# library(network)
# library(sna)
# library(ggplot2)
# 
# # random graph
# net = rgraph(10, mode = "graph", tprob = 0.5)
# net = network(net, directed = FALSE)
# 
# p <-ggnet2(net, size = 12, label = TRUE, label.alpha = 0.75, label.size = 5, color = "black", label.color = "white")
# 
# ggplotly(p)
```


https://yunranchen.github.io/intro-net-r/advanced-network-visualization.html
https://briatte.github.io/ggnet/
https://plotly.com/ggplot2/network-graphs/