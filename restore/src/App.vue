<template>
  <div id="app">
    <span>Craft</span>
    <div
      id="background-container"
      @mousehover="hover = true"
      @mouseleave="hover = false">
      <BackgroundImage
        v-for="n in 4"
        :key="n"
        :index="n - 1"
        :counter="counter"
        :hover="hover"/>
    </div>
    <p>
      The server files could not be found in the persistent volume.
      Upload a backup archive tarball to start the server.
    </p>
    <BackupUpload/>
  </div>
</template>

<script>
import BackgroundImage from '@/components/BackgroundImage.vue';
import BackupUpload from '@/components/BackupUpload.vue';

export default {
  name: 'app',
  components: {
    BackgroundImage,
    BackupUpload
  },
  data () {
    return {
      counter: 0,
      hover: false
    }
  },
  mounted () {
    setInterval(() => {
      this.counter++
    }, 10000)
  }
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css?family=Bungee&display=swap');
@import url('https://fonts.googleapis.com/css?family=Roboto+Mono&display=swap');

html, body {
  margin: 0;
  padding: 0;
}

body {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    margin-top: 10px;
    background: darken(white, 10%);
}

#app {
  width: 640px;
  height: 300px;
}

#background-container {
  position: relative;
  width: 100%;
  height: 100%;
}

span {
  font-family: 'Bungee', cursive;
  font-size: 3em;
  margin-left: 140px;
  user-select: none;
  letter-spacing: 2px;
  color: darken(white, 5%);
  text-shadow: -1px 0 #666, 0 1px #666, 1px 0 #666, 0 -1px #666;
}

// cool psuedo-selector hack
span:before {
  content: 'Nutty';
  color: lighten(black, 25%);
  text-shadow: none;
}

p {
  font-family: 'Roboto Mono', monospace;
  font-size: 1.3em;
  margin: 50px;
  color: yellow;
  text-shadow: -1px 0 #666, 0 1px #666, 1px 0 #666, 0 -1px #666;
}
</style>
