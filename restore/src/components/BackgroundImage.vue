<template>
  <div class="background" :style="styles"/>
</template>

<script>
const imageCount = 4

export default {
  props: [
    'index',
    'counter',
    'hover'
  ],
  computed: {
    styles () {
      const source = require(`@/assets/${this.index}.png`)
      return {
        'background-image': `url('${source}')`,
        'opacity': this.counter % imageCount === this.index ? 0.9 : 0,
        'transform': this.hover ? 'scale(1.03, 1.03)' : 'scale(1, 1)'
      }
    }
  }
}
</script>

<style scoped lang="scss">
.background {
    position: absolute;
    width: 100%;
    height: 100%;
    transition: all 1.0s ease-out;
    border: 6px solid lighten(black, 20%);
    outline: 3px dashed lighten(black, 20%);
    background-repeat: no-repeat;
    background-position: center;
    background-size: 640px;
}
</style>
