# Run Python script with arguments set as environmental variables
# Example usage:
# Run:
# source command_line/environmental_variables
# Run:
# ./command_line_run.sh

s="from $MODULE_NAME import $FUNC_NAME;"
s+="f=open('$STYLE_PATH','r',encoding='utf-8');"
s+="style=f.read();"
s+="svg=$FUNC_NAME(${ITEM_SCALE},${GROUP_SCALE},'${DATA_PATH}',style, -4.0, 40.3);"
s+="f=open('${DESTINATION_PATH}','w');f.write(svg)"
echo $s

python3 -c "${s}"
echo "file written to: ${DESTINATION_PATH} "
