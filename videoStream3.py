import cv2, pafy


#url = "https://youtu.be/WPrH_ivypZ8"
url = "https://manifest.googlevideo.com/api/manifest/hls_playlist/id/WPrH_ivypZ8.0/itag/95/source/yt_live_broadcast/requiressl/yes/ratebypass/yes/live/1/cmbypass/yes/goi/160/sgoap/gir%3Dyes%3Bitag%3D140/sgovp/gir%3Dyes%3Bitag%3D136/hls_chunk_host/r4---sn-gxqpgpn-h5ql.googlevideo.com/gcr/es/playlist_type/DVR/ei/new0W52qM4mk1gaE9rb4Bg/initcwndbps/13810/mm/32/mn/sn-gxqpgpn-h5ql/ms/lv/mv/m/pl/16/dover/10/keepalive/yes/fexp/23709359/mt/1530194966/disable_polymer/true/ip/138.4.32.82/ipbits/0/expire/1530216701/sparams/ip,ipbits,expire,id,itag,source,requiressl,ratebypass,live,cmbypass,goi,sgoap,sgovp,hls_chunk_host,gcr,playlist_type,ei,initcwndbps,mm,mn,ms,mv,pl/signature/3F3E7288E2B9E46B20FC04759F56A6DF27B9EF01.3C1864B2914E260A70DEDA9D04ACE652CCE5753C/key/dg_yt0/playlist/index.m3u8"

# url = "https://youtu.be/W1yKqFZ34y4" # Standard video, not live streaming
#vPafy = pafy.new(url)
#play = vPafy.getbest(preftype="webm")


cap = cv2.VideoCapture(url)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    cv2.waitKey(5)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()